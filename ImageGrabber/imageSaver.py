import os
# from datetime import datetime
from persiantools.jdatetime import JalaliDateTime
import threading

import cv2
import numpy as np
import imageio

from fileManager import fileManager


#pip install imageio[ffmpeg]
#pip install imageio imageio-ffmpeg


class imageSave:

    #image_extention = '.webp'
    #encode_param = [int(cv2.IMWRITE_WEBP_QUALITY), 90]

    image_extention = '.jpeg'
    video_extention = '.mp4'

    encode_param = [int(cv2.IMWRITE_JPEG_LUMA_QUALITY), 80]
    
    UPDATE_LIST_DIR_FPS = 100

    VIDEO_FRAME_COUNT = 100
    VIDEO_FPS = 24
    
    IMAGE_STACK = 5

    


    def __init__(self, path:str, train_id) -> None:
        self.path = path
        self.train_id = train_id
        self.start_time = {
            'left':JalaliDateTime.now(),
            'right':JalaliDateTime.now()
        }

        self.file_counter = 0
        # self.file_counter = {
        #     'left':0,
        #     'right':0
        # }

        self.file_countr = 0
        
        self.__saved_files = []
        # self.__saved_files = {
        #     'left': [],
        #     'right': []
        # }

        # self.__video_frames = {
        #     'left': [],
        #     'right': []
        # }

        self.__video:dict[str:dict] = {
            'left': {'video': None, 'frame':0},
            'right':{'video': None, 'frame':0},
        }

        self.saved_image_path = os.path.join(self.path, self.train_id)
        
        if not os.path.exists(self.saved_image_path):
            os.makedirs(self.saved_image_path) 
        
        self.__stack_images:dict[str,: dict] = {
            'left':  {'image':None, 'counter':0},
            'right': {'image':None, 'counter':0},

        }

        # self.__saved_files[name] = os.listdir(self.camera_path[name])
        self.__saved_files  = os.listdir(self.saved_image_path)


    def generate_path(self, now:JalaliDateTime):
        path = os.path.join(self.saved_image_path,
                            str(now.year),
                            str(now.month),
                            str(now.day),
                            str(now.hour),
                            str(now.minute),
                            )
        return path   

    def gen_file_name(self,now:JalaliDateTime, camera_name:str):
        #now = datetime.now()
        
        file_name = now.strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = file_name +  '_' + self.train_id + '_' + camera_name
        return file_name
    
    def save(self,camera_name:str, image):
        self.start_time[camera_name] = JalaliDateTime.now()
        file_name = self.gen_file_name(self.start_time[camera_name], camera_name)
        file_name = file_name + self.image_extention
        img_path = self.generate_path(self.start_time[camera_name])
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        img_path = os.path.join(img_path, file_name)

        

        cv2.imwrite(img_path, image, self.encode_param)

        self.file_counter +=1
        #append saved image name
        self.__saved_files.append(file_name)

    
    def save_stack(self,camera_name:str, image:np.ndarray):
        h,w = image.shape[:2]
        if self.__stack_images[camera_name]['image'] is None:
            self.start_time[camera_name] = JalaliDateTime.now()
            if len(image.shape) == 2:
                self.__stack_images[camera_name]['image'] = np.zeros((h*self.IMAGE_STACK, w))
            else:
                self.__stack_images[camera_name]['image'] = np.zeros((h*self.IMAGE_STACK, w, 3))


        res:np.ndarray = self.__stack_images[camera_name]['image']
        cnt = self.__stack_images[camera_name]['counter']
        res[cnt * h: (cnt+1)*h, :,:] = image
        cnt+=1

        

        if cnt >= self.IMAGE_STACK:
            file_name = self.gen_file_name(self.start_time[camera_name], camera_name)
            file_name = file_name + self.image_extention
            img_path = self.generate_path(self.start_time[camera_name])
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            img_path = os.path.join(img_path, file_name)
            cv2.imwrite(img_path, res, self.encode_param)

            self.__stack_images[camera_name]['image'] = None
            self.__stack_images[camera_name]['counter'] = 0

            self.file_counter +=1
            #append saved image name
            self.__saved_files.append(file_name)
        
        else:
            self.__stack_images[camera_name]['image'] = res
            cnt = self.__stack_images[camera_name]['counter'] = cnt




    def save_video(self, camera_name:str, image:np.ndarray):

        if self.__video[camera_name]['video'] is None or self.__video[camera_name]['frame'] > self.VIDEO_FRAME_COUNT:
            if self.__video[camera_name]['video'] is not None:
                prev_video = self.__video[camera_name]['video']
                prev_video.close()
                threading.Thread(target=prev_video.close).start()
                

            file_name = self.gen_file_name()
            file_name = file_name + self.video_extention

            file_name = self.gen_file_name(self.start_time[camera_name], camera_name)
            file_name = file_name + self.image_extention
            video_path = self.generate_path(self.start_time[camera_name])
            if not os.path.exists(video_path):
                os.makedirs(video_path)
            video_path = os.path.join(video_path, file_name)

            self.__saved_files.append(file_name)


            self.__video[camera_name]['video'] =  imageio.get_writer(video_path, fps=self.VIDEO_FPS, codec='libx264')

            self.__video[camera_name]['frame'] = 0
            
            print('video writer create')

            self.file_counter +=1
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.__video[camera_name]['frame']==0:
            self.start_time[camera_name] = JalaliDateTime.now()
        
        self.__video[camera_name]['video'].append_data(image)
        self.__video[camera_name]['frame'] +=1
        

    
        #self.__video[camera_name]['video'].write(image)

    def remove_base_on_count(self, max_count=10):
        # #-------------------
        if self.file_countr > self.UPDATE_LIST_DIR_FPS:
            self.file_countr = 0
            self.__saved_files = os.listdir(self.saved_image_path)
            self.__saved_files.sort()
            print('update list dir')
        #-------------------
        count = len(self.__saved_files)
        if count > max_count:
            for i in range(count - max_count):
                try:
                    img_path = os.path.join(self.saved_image_path, self.__saved_files[0])
                    fileManager.delete_file(img_path)
                    self.__saved_files.pop(0)
                except Exception as e:
                    print(e)
        




        


if __name__ == '__main__':
    ims = imageSave('images')