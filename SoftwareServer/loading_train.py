import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar
from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtGui import QPixmap, QPalette, QColor, QPainter

class LoadingWindow(QWidget):
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # No window title or border, always on top

        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background

        # Set window size and initial position
        self.setFixedSize(500, 100)

        # Progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setFixedHeight(10)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: rgba(200, 200, 200, 150);
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #3b5998;
                border-radius: 5px;
            }
        """)

        # Train image
        self.train_pixmap = QPixmap("icons/icons8-railway-50.png")
        self.train_position = 0  # Initial train position

        # Percentage label
        self.percent_label = QLabel("0%", self)
        self.percent_label.setAlignment(Qt.AlignCenter)
        self.percent_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.percent_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # Set background color (optional)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0, 0))  # Fully transparent
        self.setPalette(palette)

        # Initialize loading process
        self.progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Update every 50ms



        self.center_on_parent(parent)

    def center_on_parent(self, parent):
        if parent is not None:
            # Calculate the center position
            parent_geometry = parent.geometry()
            x = parent_geometry.x() + (parent_geometry.width() - self.width()) // 2
            y = parent_geometry.y() + (parent_geometry.height() - self.height()) // 2
            self.move(x, y)




    def update_progress(self):
        self.progress += 1
        self.progress_bar.setValue(self.progress)
        self.percent_label.setText(f"{self.progress}%")

        # Update the train's position based on progress
        bar_width = self.progress_bar.width()
        max_train_x = bar_width - self.train_pixmap.width()
        self.train_position = max_train_x * self.progress / 100.0

        self.update()  # Trigger the paintEvent to redraw the train

        if self.progress >= 100:
            self.timer.stop()
            self.close()  # Close the loading screen when complete

    def paintEvent(self, event):
        painter = QPainter(self)
        # Draw the train above the progress bar
        # Ensure that the train image is fully visible above the progress bar
        train_y_position = self.progress_bar.y() - self.train_pixmap.height() +5  # Adjust vertical offset as needed
        painter.drawPixmap(QPoint(int(self.train_position), train_y_position), self.train_pixmap)  

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoadingWindow()
    window.show()

    sys.exit(app.exec())
