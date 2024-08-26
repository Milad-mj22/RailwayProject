import os
import cv2
from persiantools.jdatetime import JalaliDateTime


class ImagePLayer:

    def __init__(self, path:str) -> None:
        self.path = path
        self.hour_idx = 0
        self.minute_idx = 0
        self.image_idx = 0
    
        self.minutes = []
        self.images = []

    def load_availables_hours_folder(self,):
        self.houres = os.listdir(self.path)
        self.houres.sort()


    def load_availables_minutes_folder(self,):
        current_houre = self.houres[self.hour_idx]
        path = os.path.join(path, str(current_houre))
        self.minutes = os.listdir(path)
        self.minutes.sort()

    def load_availables_images(self,):
        current_houre = self.houres[self.hour_idx]
        current_minute = self.minutes[self.minute_idx]

        path = os.path.join(path, str(current_houre), str(current_minute))
        self.images = os.listdir(path)
        self.images.sort()
    
    def extract_file_name_info(name:str) -> tuple[JalaliDateTime, str, str]:
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name

    def next(self,):
        self.image_idx +=1
        if self.image_idx > len(self.images):
            self.image_idx=0
            self.minute_idx+=1

            if self.minute_idx > len(self.minutes):
                self.hour_idx+=1

                if self.hour_idx > len(self.houres):
                    return None, True
                
                self.load_availables_minutes_folder()
            self.load_availables_images()

        current_houre = self.houres[self.hour_idx]
        current_minute = self.minutes[self.minute_idx]
        current_image = self.images[self.image_idx]
        path = os.path.join(self.path, 
                            str(current_houre),
                            str(current_minute),
                            str(current_image))
        img = cv2.imread(path)
        return img, False
                
    def set_time(self, h:int,m:int, s:int):
        self.hour_idx = self.houres.index(str(h))
        self.load_availables_minutes_folder()

        self.minute_idx = self.houres.index(str(m))

        self.load_availables_images()

        for i,fname in enumerate(self.images):
            dt:JalaliDateTime
            dt, _,_ = self.extract_file_name_info(fname)
            if abs(dt.second - s) <=1:
                self.image_idx = i
                break
            elif dt.second > s:
                self.image_idx = i
                break
