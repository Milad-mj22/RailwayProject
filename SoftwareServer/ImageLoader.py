
import sys
import os
import time
import threading
from threading import Thread, Event
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer, Signal, QObject
from PySide6.QtGui import QPixmap



class ImageLoader(QObject,Thread):
    image_signal = Signal(QPixmap)  # Signal to emit the loaded image

    def __init__(self,stop_event, folder_path, fps=7):
        super().__init__()
        self.folder_path = folder_path
        # self.image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))])
        self.current_image_index = 0
        self.fps = fps
        self.running = True
        self.playing = False
        
        self.stop_event = stop_event

    

    def run(self):
            
        while not self.stop_event.is_set():

            self.playing = True

            try:

                if os.path.exists(self.folder_path) and os.path.isdir(self.folder_path):
                    for hour in os.listdir(self.folder_path):
                        hour_path = os.path.join(self.folder_path,hour)
                        if os.path.exists(hour_path) and os.path.isdir(hour_path):
                            for minute in os.listdir(hour_path):
                                print('os.listdir(hour_path)',os.listdir(hour_path))

                                minute_path = os.path.join(hour_path,minute)
                                if os.path.exists(minute_path) and os.path.isdir(minute_path) and len(os.listdir(minute_path))>1:
                           
                                    
                                    # for img in os.listdir(minute_path):
                                    image_files = sorted([f for f in os.listdir(minute_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))])
                                    for img in image_files:

                                        if self.stop_event.is_set():
                      
                                            break  # Exit the inner loop


                                        image_path = os.path.join(minute_path,img)
                                        pixmap = QPixmap(image_path)

                                        # Emit the signal with the loaded image
                                        self.image_signal.emit(pixmap)

                                        # Sleep to maintain the desired FPS
                                        time.sleep(1 / self.fps)
                                if self.stop_event.is_set():
                                    print("Worker stopped.")
                                    break  # Exit the outer loop if stop_event is set
                        if self.stop_event.is_set():
                                print("Worker stopped.")
                                break  # Exit the outer loop if stop_event is set

                else:
                    print(f"{self.folder_path} is not a directory or does not exist.")
                    time.sleep(1 / self.fps)
            
            except Exception as e:
                print('Error : ',e)



            self.playing = False


    def stop(self):
        self.running = False

        self._stop_requested = True
        self.join()  # Wait for the thread to finish



    def update_fps(self,speed_rate):
        self.fps = speed_rate


    def update_folder_path(self,folder_path):
        self.folder_path = folder_path



    def __load_image_path__(self,folder_path):


        pathes = []


        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for hour in os.listdir(folder_path):
                hour_path = os.path.join(folder_path,hour)
                if os.path.exists(hour_path) and os.path.isdir(hour_path):
                    for minute in os.listdir(hour_path):
                        minute_path = os.path.join(hour_path,minute)
                        print(minute_path)
                        if os.path.exists(minute_path) and os.path.isdir(minute_path) and len(os.listdir(minute_path)>1):
                            path = os.path.join(hour,minute)
                            pathes.append(path)





                        else:
                            print(f"{minute_path} is not a directory or does not exist or len < 1.")
                else:
                    print(f"{hour_path} is not a directory or does not exist.")
        else:
            print(f"{folder_path} is not a directory or does not exist.")

        return pathes
    


    # def __path_generator__(self):

        