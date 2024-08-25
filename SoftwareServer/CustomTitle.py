
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #2a2a2a; color: white;")  # Custom background and text color

        self.setFixedHeight(30)  # Height of the custom title bar

        # Title label
        self.title_label = QLabel("Custom Title Bar", self)
        self.title_label.setAlignment(Qt.AlignCenter)

        # Minimize, Maximize, Close buttons
        self.btn_minimize = QPushButton("_", self)
        # self.btn_minimize.clicked.connect(parent.showMinimized)

        self.btn_maximize = QPushButton("☐", self)
        self.btn_maximize.clicked.connect(self.toggle_maximize_restore)

        self.btn_close = QPushButton("X", self)
        # self.btn_close.clicked.connect(parent.close)

        # Button styles
        button_style = "background-color: #2a2a2a; color: white; border: none; padding: 5px;"
        self.btn_minimize.setStyleSheet(button_style)
        self.btn_maximize.setStyleSheet(button_style)
        self.btn_close.setStyleSheet(button_style)

        # Layout for buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.btn_minimize)
        buttons_layout.addWidget(self.btn_maximize)
        buttons_layout.addWidget(self.btn_close)

        # Main layout for the title bar
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(buttons_layout)
        main_layout.setContentsMargins(5, 0, 5, 0)

        self.setLayout(main_layout)

        # self.parent().installEventFilter(self)  # To handle window drag

    def toggle_maximize_restore(self):
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()

    def eventFilter(self, obj, event):
        if obj == self.parent() and event.type() == event.Resize:
            self.title_label.setFixedWidth(self.width() - self.btn_minimize.width() - self.btn_maximize.width() - self.btn_close.width())
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent().move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()