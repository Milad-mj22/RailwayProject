import threading
import queue
import time

from persiantools.jdatetime import JalaliDateTime
import cv2


THREAD = False

class Camera:
    MAX_ERROR_COUNT = 5
    TIME_OUT = 2

    

    def __init__(self,name:str, username:str, password:str, ip:str) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.ip = ip
        self.stream_url = self.get_stream_url()
        self.grabb_image_func = None
        self.vCap = None

        #self.__play_flag = threading.Event()
        #self.__play_flag.set()  # Set the flag to True initially
        self.__play_flag = True
        self.lockVcap = threading.Lock()
        
        self.open_camera_thread = None
        self.grabbing_thread = None

    def get_stream_url(self,):
        url = f'rtsp://{self.username}:{self.password}@{self.ip}:554/mainstream1'
        return url
    

    def connect(self,):
        print('trying connect to camera...')
        if THREAD:
            self.open_camera_thread = threading.Thread(target=self.__build_camera, daemon=True)
            self.open_camera_thread.start()
            self.open_camera_thread.join()

        else:
            self.__build_camera()

        self.connect_evet()
        
            

        
            
    def connect_evet(self,):
        print('camera connect evet')
        self.grabbing()
    

    def disconnect_evet(self,):
        print('camera disconnect evet!')
        if self.vCap is not None:
            self.vCap.release()
            self.vCap = None
        time.sleep(2)
        cv2.destroyAllWindows()
        self.connect()
            
        
    
    def __build_camera(self):
        self.vCap = None

        while True:
            #self.vCap = cv2.VideoCapture(self.stream_url)
            self.vCap = cv2.VideoCapture(0)
          
            if self.vCap.isOpened():
                print('Camera is connected')
                break
            else:
                print('release')
                self.vCap.release()
                self.vCap = None
                time.sleep(5)
            
            # time.sleep(1)
                
                
        
        

    def set_grabb_image_callback(self, func):
        self.grabb_image_func = func

    def grabbing(self,):

        if THREAD:
            if self.grabbing_thread and self.grabbing_thread.is_alive():
                print("Grabbing is already in progress.")
                return
            
            self.__play_flag = True
            self.grabbing_thread = threading.Thread(target=self.__grabbing, daemon=True)
            self.grabbing_thread.start()
        
        else:
            self.__grabbing()
        

    def stop(self,):
        self.__play_flag = False
        #self.grabbing_thread.join()

    def __grabbing(self,):
        self.count_error = 0
        while self.__play_flag:
            # try:
            if THREAD:
                with self.lockVcap:
                    ret, image = self.vCap.read()
            else:
                ret, image = self.vCap.read()
            
            if not ret:
                self.count_error +=1

                if self.count_error > self.MAX_ERROR_COUNT:        
                    break
                continue

            self.count_error = 0
            if self.grabb_image_func is not None:
                self.grabb_image_func(self.name, image)

        if THREAD:
            threading.Thread( target=self.disconnect_evet, daemon=True).start()
            print('finish grabbing')
        else:
            self.disconnect_evet()

if __name__ == '__main__':

    "rtsp://admin:Milad1375422@@192.168.1.13:554/stream1"

    cam = Camera('admin','Milad1375422@', '192.168.1.13')
    cam.connect()

    #cam.grabbing()