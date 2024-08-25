import cv2
import numpy as np

from camera import Camera
from imageSaver import imageSave
from configReader import configReader 
from fileManager import fileManager, PERMITION
import os


WEBCAM_DEBUG = True

class App:

    def __init__(self) -> None:
        self.config = configReader()
        self.isaver = imageSave(self.config.path, self.config.train_id)
        self.cameras = {}

        self.last_image = {
            'left': None,
            'right': None
        }

        try:
            fileManager.remove_share(share_name='images')
            fileManager.create_and_share_folder(os.path.abspath(self.config.path), 
                                                share_name='images', 
                                                permissions=PERMITION)
        except Exception as e:
            print(e)

        self.isaver.VIDEO_FPS = self.config.video_fps
        self.isaver.VIDEO_FRAME_COUNT = self.config.video_frames_count



        

    def load_camera(self,):
        for camera_info in self.config.cameras:
            cam = Camera(camera_info['name'], camera_info['username'], camera_info['password'], camera_info['ip'])
            self.cameras[camera_info['name']] = cam
            cam.set_grabb_image_callback(self.grab_image_event)
            cam.connect()

    def is_motion(self, camera_name:str, image):
        if self.last_image[camera_name] is not None:
            diff = cv2.absdiff(self.last_image[camera_name], image)
            self.last_image[camera_name] = image

            _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
            changed_pixel = np.sum(thresh) / 255
            if changed_pixel > self.config.motion_sens:
                return True
            return False
        else:
            self.last_image[camera_name] = image
            return True


    
    def grab_image_event(self, cam_name:str, image):
        image = cv2.resize(image, (1920,1080))
        cv2.imshow(cam_name, image)        
        cv2.waitKey(5)
        if self.config.motion:
            if not self.is_motion(cam_name, image):
                return
        
        if self.config.output_type == 'image':
            self.isaver.save(cam_name, image)
        
        elif self.config.output_type == 'stack_image':
            self.isaver.save_stack(cam_name, image)
        
        else:
            self.isaver.save_video(cam_name, image)
        # 

        self.isaver.remove_base_on_count(self.config.max_file_count)




app = App()
app.load_camera()


#while True:
#    pass