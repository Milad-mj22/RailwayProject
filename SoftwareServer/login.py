import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6 import QtCore as sQtCore




class LoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        # Remove window close button and add rounded corners
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.pos_ = self.pos()
        self._old_pos = None
        # Create widgets
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password input

        self.open_button = QPushButton('Login', self)
        self.close_button = QPushButton('Close', self)

        # Set up layouts
        main_layout = QVBoxLayout()

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.close_button)

        main_layout.addLayout(password_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Set styles
        self.setStyleSheet("""
            QWidget#LoginPage {
                background-color: #f0f0f0;
                border-radius: 15px;
                border: 2px solid #ccc;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #fff;
            }
            QPushButton {
                font-size: 14px;
                padding: 5px 10px;
                border: 1px solid #007BFF;
                border-radius: 5px;
                background-color: #007BFF;
                color: white;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #003d80;
            }
        """)

        # Connect buttons
        self.open_button.clicked.connect(self.open_button_clicked)
        self.close_button.clicked.connect(self.close_button_clicked)

        self.setWindowTitle('Login Page')
        self.setGeometry(300, 150, 300, 150)
        self.show()
        self.centerOnParent()

        
    def centerOnParent(self):
        if self.parent():
            parent_geometry = self.parent().geometry()
            self_geometry = self.frameGeometry()
            center_point = parent_geometry.center()
            self_geometry.moveCenter(center_point)
            self.move(self_geometry.topLeft())


    # def mousePressEvent(self, event):
    #     if event.button() == sQtCore.Qt.LeftButton and not self.isMaximized():

    #         self._old_pos = event.globalPosition().toPoint()

    # def mouseReleaseEvent(self, event):
    #     if event.button() == sQtCore.Qt.LeftButton:
    #         self._old_pos = None

    # def mouseMoveEvent(self, event):
    #     if not self._old_pos:
    #         return
    #     delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self._old_pos = event.globalPosition().toPoint()




    def open_button_clicked(self):
        # Implement the open button functionality here
        self.password = self.password_input.text()
        print("Open button clicked")

    def close_button_clicked(self):
        # Implement the close button functionality here
        print("Close button clicked")
        self.close()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    sys.exit(app.exec())
