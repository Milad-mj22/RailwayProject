import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog, QSlider
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPixmap, QPainter, QColor
from persiantools.jdatetime import JalaliDateTime

class ImageSlider(QSlider):
    def __init__(self, parent=None, mode=24,  fps=24):
        super().__init__(Qt.Horizontal, parent)
        self.exists_times = []
        self.mode = mode

        self.total_time= self.mode * 3600
        

        self.fps = fps

    def setImagePositions(self, exists_times:list[tuple[JalaliDateTime]]):
        self.exists_times = exists_times
        self.update()



    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        slider_rect = self.geometry()

        painter.fillRect(QRect(0, 0,slider_rect.width() , slider_rect.height()), QColor('red'))

        for start_time, end_time in self.exists_times:
            
            delat = end_time - start_time
            if self.mode == 24:
                x1_sec = start_time.hour * 3600 + start_time.minute - 60 + start_time.second
            elif self.mode == 1:
                x1_sec =  start_time.minute - 60 + start_time.second

            width_sec = delat.total_seconds()  

            x1 = int(x1_sec / self.total_time * slider_rect.width())
            width = int(width_sec / self.total_time * slider_rect.width())

            painter.fillRect(QRect(x1, 0,width , slider_rect.height()), QColor('green'))
            

class ImagePlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Player")
        self.setGeometry(350, 100, 700, 500)

        self.init_ui()

        self.image_files = []
        self.current_index = 0

        
        

        self.show()

    def init_ui(self):
        # Create a QLabel to display images
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: black;")

        # Create a custom slider
        self.slider = ImageSlider()
        self.slider.setRange(0, 1000)
        self.slider.sliderMoved.connect(self.set_position)

        # Create a layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.slider)

        # Create a container widget
        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        # Create open button
        open_btn = QPushButton("Open Folder")
        open_btn.clicked.connect(self.open_folder)
        self.layout.addWidget(open_btn)

        # Set up a timer to update the image
        self.timer = QTimer(self)
        self.timer.setInterval(40)  # 1000ms / 25fps = 40ms per frame
        self.timer.timeout.connect(self.update_image)
        self.timer.start()

        add = False

        exists_times = []
        for h in range(1,12):
            for minute in range(0,50,5):
        #         # for second in range(0,59):
        #             # for micro in range(0,1000000,50000):

        #                 # add = not(add)

        #                 # if add:

        #                     now = JalaliDateTime.now()
        #                     now = now.replace(hour=h,minute=minute,second=0,microsecond=0)
        #                     exists_times.append(now)
                try:
                    start = JalaliDateTime.now()
                    start = start.replace(hour=h,minute=minute)
                    end = start.replace(minute=start.minute + 5)
                    exists_times.append((start,end))
                except:
                    pass

        self.slider.setImagePositions(exists_times)

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Open Folder", "", QFileDialog.ShowDirsOnly)
        if folder:
            self.image_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
            self.image_files.sort()
            self.current_index = 0

            # Update the slider with the image positions
            self.update_slider()

    def update_image(self):
        if self.image_files:
            pixmap = QPixmap(self.image_files[self.current_index])
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            self.current_index = (self.current_index + 1) % len(self.image_files)
            self.slider.setValue(self.current_index)

    def set_position(self, position):
        self.current_index = position

    def update_slider(self):
        positions = [1 if os.path.exists(file) else 0 for file in self.image_files]
        self.slider.setImagePositions(positions)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = ImagePlayer()
    sys.exit(app.exec_())
