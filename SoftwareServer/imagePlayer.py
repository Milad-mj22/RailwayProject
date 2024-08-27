import os
import cv2
from persiantools.jdatetime import JalaliDateTime
from PySide6.QtCore import Qt, QTimer, Signal, QObject
from PySide6.QtGui import QPixmap
import time

class ImagePLayer:

    def __init__(self, path:str) -> None:
        self.path = path
        self.hour_idx = 0
        self.minute_idx = 0
        self.image_idx = 0

        self.houres = []
        self.minutes = []
        self.images = []

        self.load_availables_hours_folder()
        self.load_availables_minutes_folder()
        self.load_availables_images()

    def load_availables_hours_folder(self,):
        self.houres = os.listdir(self.path)
        self.houres.sort(key= lambda x:int(x))


    def load_availables_minutes_folder(self,):
        current_houre = self.houres[self.hour_idx]
        path = os.path.join(self.path, str(current_houre))
        self.minutes = os.listdir(path)
        self.minutes.sort(key= lambda x:int(x))

    def load_availables_images(self,):
        current_houre = self.houres[self.hour_idx]
        current_minute = self.minutes[self.minute_idx]

        path = os.path.join(self.path, str(current_houre), str(current_minute))
        self.images = os.listdir(path)
        self.images.sort()
    
    def extract_file_name_info(self,name:str) -> tuple[JalaliDateTime, str, str]:
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name

    def next(self,):
        self.image_idx +=1
        if self.image_idx >= len(self.images):
            self.image_idx=0
            self.minute_idx+=1

            if self.minute_idx >= len(self.minutes):
                self.hour_idx+=1
                self.minute_idx = 0

                if self.hour_idx >= len(self.houres):
                    return None, True, None,None
                                
                self.load_availables_minutes_folder()
            self.load_availables_images()

        current_houre = self.houres[self.hour_idx]
        current_minute = self.minutes[self.minute_idx]
        current_image = self.images[self.image_idx]

        dt,_,_ = self.extract_file_name_info(current_image)
        path = os.path.join(self.path, 
                            str(current_houre),
                            str(current_minute),
                            str(current_image))
        t =time.time()
        # img = cv2.imread(path)
        img = None
        # print('read',time.time()-t)
        
        return img, False, dt,path
                
    def set_time(self, h:int,m:int, s:int):
        self.hour_idx = self.houres.index(str(h))
        self.load_availables_minutes_folder()

        self.minute_idx = self.minutes.index(str(m))

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




class WorkerImagePlayer(QObject):
    finish_signal = Signal()
    refresh_signal = Signal()

    def __init__(self, refresh_rate=1, name='') -> None:
        super().__init__()
        self.refresh_rate = refresh_rate
        self.name = name
        self.__start_time = 0
        self.__running_flag = True

    
    def set_refresh_rate(self,refresh_date:int):

        self.refresh_rate = refresh_date



    def stop(self,):
        self.__running_flag = False



    
    def run_loop(self,):
        while self.__running_flag:
  
            self.refresh_signal.emit()        
            if self.__running_flag:
                self.finish_signal.emit()

            time.sleep(round(1/self.refresh_rate,5))
            


