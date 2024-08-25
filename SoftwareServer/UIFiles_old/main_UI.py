# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 742)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(98, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftSideFrame = QFrame(self.frame)
        self.leftSideFrame.setObjectName(u"leftSideFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSideFrame.sizePolicy().hasHeightForWidth())
        self.leftSideFrame.setSizePolicy(sizePolicy)
        self.leftSideFrame.setMinimumSize(QSize(0, 0))
        self.leftSideFrame.setMaximumSize(QSize(95, 16777211))
        self.leftSideFrame.setStyleSheet(u"background-color: #17203A;")
        self.leftSideFrame.setFrameShape(QFrame.StyledPanel)
        self.leftSideFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.leftSideFrame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.dorsa_lbl = QLabel(self.leftSideFrame)
        self.dorsa_lbl.setObjectName(u"dorsa_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dorsa_lbl.sizePolicy().hasHeightForWidth())
        self.dorsa_lbl.setSizePolicy(sizePolicy1)
        self.dorsa_lbl.setMinimumSize(QSize(96, 45))
        self.dorsa_lbl.setMaximumSize(QSize(50, 65))
        self.dorsa_lbl.setPixmap(QPixmap(u"../../camera_recorder/copy/assets/icons/2.png"))
        self.dorsa_lbl.setScaledContents(True)
        self.dorsa_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.dorsa_lbl)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer)

        self.btn_side_playback = QPushButton(self.leftSideFrame)
        self.btn_side_playback.setObjectName(u"btn_side_playback")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_side_playback.sizePolicy().hasHeightForWidth())
        self.btn_side_playback.setSizePolicy(sizePolicy2)
        self.btn_side_playback.setMinimumSize(QSize(0, 50))
        self.btn_side_playback.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_side_playback.setFont(font1)
        self.btn_side_playback.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_playback.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/live_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_playback.setIcon(icon)
        self.btn_side_playback.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.btn_side_playback)

        self.btn_side_download = QPushButton(self.leftSideFrame)
        self.btn_side_download.setObjectName(u"btn_side_download")
        sizePolicy2.setHeightForWidth(self.btn_side_download.sizePolicy().hasHeightForWidth())
        self.btn_side_download.setSizePolicy(sizePolicy2)
        self.btn_side_download.setMinimumSize(QSize(0, 50))
        self.btn_side_download.setMaximumSize(QSize(16777215, 50))
        self.btn_side_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_download.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_download.setIcon(icon1)
        self.btn_side_download.setIconSize(QSize(30, 30))

        self.verticalLayout_67.addWidget(self.btn_side_download)

        self.btn_side_settings = QPushButton(self.leftSideFrame)
        self.btn_side_settings.setObjectName(u"btn_side_settings")
        sizePolicy2.setHeightForWidth(self.btn_side_settings.sizePolicy().hasHeightForWidth())
        self.btn_side_settings.setSizePolicy(sizePolicy2)
        self.btn_side_settings.setMinimumSize(QSize(0, 50))
        self.btn_side_settings.setMaximumSize(QSize(16777215, 50))
        self.btn_side_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_settings.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_settings.setIcon(icon2)
        self.btn_side_settings.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.btn_side_settings)

        self.btn_side_aboutus = QPushButton(self.leftSideFrame)
        self.btn_side_aboutus.setObjectName(u"btn_side_aboutus")
        sizePolicy2.setHeightForWidth(self.btn_side_aboutus.sizePolicy().hasHeightForWidth())
        self.btn_side_aboutus.setSizePolicy(sizePolicy2)
        self.btn_side_aboutus.setMinimumSize(QSize(0, 50))
        self.btn_side_aboutus.setMaximumSize(QSize(16777215, 50))
        self.btn_side_aboutus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_aboutus.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_side_aboutus.setIcon(icon2)
        self.btn_side_aboutus.setIconSize(QSize(35, 35))

        self.verticalLayout_67.addWidget(self.btn_side_aboutus)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_2)

        self.dorsa_lbl_2 = QLabel(self.leftSideFrame)
        self.dorsa_lbl_2.setObjectName(u"dorsa_lbl_2")
        sizePolicy1.setHeightForWidth(self.dorsa_lbl_2.sizePolicy().hasHeightForWidth())
        self.dorsa_lbl_2.setSizePolicy(sizePolicy1)
        self.dorsa_lbl_2.setMinimumSize(QSize(91, 75))
        self.dorsa_lbl_2.setMaximumSize(QSize(106, 87))
        self.dorsa_lbl_2.setPixmap(QPixmap(u"icons/download.png"))
        self.dorsa_lbl_2.setScaledContents(True)
        self.dorsa_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.dorsa_lbl_2)

        self.verticalLayout_67.setStretch(3, 10)
        self.verticalLayout_67.setStretch(5, 10)
        self.verticalLayout_67.setStretch(6, 28)

        self.horizontalLayout_2.addWidget(self.leftSideFrame)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 69))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_playback = QWidget()
        self.page_playback.setObjectName(u"page_playback")
        self.horizontalLayout_3 = QHBoxLayout(self.page_playback)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.page_playback)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(320, 0))
        self.frame_4.setMaximumSize(QSize(320, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(73, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(self.frame_10)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 300))
        self.verticalLayout_24 = QVBoxLayout(self.groupBox)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.calendar_widget = QWidget(self.groupBox)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.calendar_widget)

        self.frame_43 = QFrame(self.groupBox)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 50))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_date_2 = QLabel(self.frame_43)
        self.label_date_2.setObjectName(u"label_date_2")
        self.label_date_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_30.addWidget(self.label_date_2)

        self.label_date = QLabel(self.frame_43)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_30.addWidget(self.label_date)


        self.verticalLayout_24.addWidget(self.frame_43)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 45))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_6.addWidget(self.frame_11)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.line_4 = QFrame(self.page_playback)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.frame_6 = QFrame(self.page_playback)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(2, 1))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"icons/2024-07-30_09-20-23-005523__11BG21.jpeg"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_8)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.line_3 = QFrame(self.frame_8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.frame_42 = QFrame(self.frame_8)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_24 = QLabel(self.frame_42)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_29.addWidget(self.label_24)


        self.horizontalLayout_4.addWidget(self.frame_42)


        self.verticalLayout_5.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_23.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_playback)
        self.page_download = QWidget()
        self.page_download.setObjectName(u"page_download")
        self.horizontalLayout_6 = QHBoxLayout(self.page_download)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_12 = QFrame(self.page_download)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(316, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_2 = QGroupBox(self.frame_12)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_18 = QFrame(self.groupBox_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.checkBox_4 = QCheckBox(self.frame_18)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.comboBox_7 = QComboBox(self.frame_19)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_8.addWidget(self.comboBox_7)

        self.pushButton_6 = QPushButton(self.frame_19)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.comboBox_3 = QComboBox(self.frame_19)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_8.addWidget(self.comboBox_3)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.groupBox_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox = QCheckBox(self.frame_17)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_11.addWidget(self.checkBox)

        self.frame_13 = QFrame(self.frame_17)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.frame_13)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_7.addWidget(self.comboBox_2)


        self.verticalLayout_11.addWidget(self.frame_13)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_14 = QFrame(self.groupBox_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_2 = QCheckBox(self.frame_14)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_9.addWidget(self.checkBox_2)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_21)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.frame_21)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_10.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.frame_21)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_10.addWidget(self.toolButton)


        self.verticalLayout_9.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.frame_22)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.frame_22)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.toolButton_2 = QToolButton(self.frame_22)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_11.addWidget(self.toolButton_2)


        self.verticalLayout_9.addWidget(self.frame_22)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.groupBox_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_3 = QCheckBox(self.frame_15)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_10.addWidget(self.checkBox_3)

        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.timeEdit = QTimeEdit(self.frame_23)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.horizontalLayout_12.addWidget(self.timeEdit)


        self.verticalLayout_10.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.frame_24)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.timeEdit_2 = QTimeEdit(self.frame_24)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.horizontalLayout_13.addWidget(self.timeEdit_2)


        self.verticalLayout_10.addWidget(self.frame_24)


        self.verticalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_13.addWidget(self.groupBox_2)

        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_13.addWidget(self.pushButton_5)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_14.addWidget(self.frame_20)


        self.verticalLayout_13.addWidget(self.frame_16)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_44 = QFrame(self.page_download)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_44)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.tableWidget = QTableWidget(self.frame_44)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_25.addWidget(self.tableWidget)

        self.progressBar = QProgressBar(self.frame_44)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_25.addWidget(self.progressBar)


        self.horizontalLayout_6.addWidget(self.frame_44)

        self.stackedWidget.addWidget(self.page_download)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_15 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_25 = QFrame(self.page_settings)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_25)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_25)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.verticalLayout_17 = QVBoxLayout(self.add)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_31 = QFrame(self.add)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)

        self.name_input = QLineEdit(self.frame_31)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMaximumSize(QSize(140, 16777215))
        self.name_input.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_20.addWidget(self.name_input)


        self.verticalLayout_17.addWidget(self.frame_31)

        self.line_5 = QFrame(self.add)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_5)

        self.frame_33 = QFrame(self.add)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.frame_33)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.city_input = QLineEdit(self.frame_33)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setMaximumSize(QSize(140, 16777215))
        self.city_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.horizontalLayout_21.addWidget(self.city_input)


        self.verticalLayout_17.addWidget(self.frame_33)

        self.line_6 = QFrame(self.add)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_6)

        self.frame_30 = QFrame(self.add)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(self.frame_30)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.ip_input = QLineEdit(self.frame_30)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMaximumSize(QSize(140, 16777215))
        self.ip_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.horizontalLayout_18.addWidget(self.ip_input)


        self.verticalLayout_17.addWidget(self.frame_30)

        self.line_7 = QFrame(self.add)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_7)

        self.frame_28 = QFrame(self.add)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.username_input = QLineEdit(self.frame_28)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_16.addWidget(self.username_input)


        self.verticalLayout_17.addWidget(self.frame_28)

        self.line_8 = QFrame(self.add)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_8)

        self.frame_29 = QFrame(self.add)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.frame_29)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.password_input = QLineEdit(self.frame_29)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_17.addWidget(self.password_input)


        self.verticalLayout_17.addWidget(self.frame_29)

        self.btn_add_check_connection = QPushButton(self.add)
        self.btn_add_check_connection.setObjectName(u"btn_add_check_connection")

        self.verticalLayout_17.addWidget(self.btn_add_check_connection)

        self.btn_save_add = QPushButton(self.add)
        self.btn_save_add.setObjectName(u"btn_save_add")

        self.verticalLayout_17.addWidget(self.btn_save_add)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.textEdit_ping_status = QTextEdit(self.add)
        self.textEdit_ping_status.setObjectName(u"textEdit_ping_status")

        self.verticalLayout_17.addWidget(self.textEdit_ping_status)

        self.tabWidget.addTab(self.add, "")
        self.modify = QWidget()
        self.modify.setObjectName(u"modify")
        self.verticalLayout_20 = QVBoxLayout(self.modify)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_35 = QFrame(self.modify)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_35)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.comboBox_systems = QComboBox(self.frame_35)
        self.comboBox_systems.setObjectName(u"comboBox_systems")

        self.verticalLayout_18.addWidget(self.comboBox_systems)


        self.verticalLayout_20.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.modify)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_system_edit = QPushButton(self.frame_34)
        self.btn_system_edit.setObjectName(u"btn_system_edit")
        self.btn_system_edit.setLocale(QLocale(QLocale.English, QLocale.Tanzania))

        self.horizontalLayout_22.addWidget(self.btn_system_edit)

        self.btn_system_delete = QPushButton(self.frame_34)
        self.btn_system_delete.setObjectName(u"btn_system_delete")

        self.horizontalLayout_22.addWidget(self.btn_system_delete)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.line_2 = QFrame(self.modify)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_2)

        self.frame_modify = QFrame(self.modify)
        self.frame_modify.setObjectName(u"frame_modify")
        self.frame_modify.setFrameShape(QFrame.StyledPanel)
        self.frame_modify.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_modify)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.frame_40 = QFrame(self.frame_modify)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.frame_40)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_27.addWidget(self.label_22)

        self.name_input_modify = QLineEdit(self.frame_40)
        self.name_input_modify.setObjectName(u"name_input_modify")
        self.name_input_modify.setMaximumSize(QSize(140, 16777215))
        self.name_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_27.addWidget(self.name_input_modify)


        self.verticalLayout_19.addWidget(self.frame_40)

        self.line_9 = QFrame(self.frame_modify)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_9)

        self.frame_36 = QFrame(self.frame_modify)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.frame_36)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.city_input_modify = QLineEdit(self.frame_36)
        self.city_input_modify.setObjectName(u"city_input_modify")
        self.city_input_modify.setMaximumSize(QSize(140, 16777215))
        self.city_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_23.addWidget(self.city_input_modify)


        self.verticalLayout_19.addWidget(self.frame_36)

        self.line_10 = QFrame(self.frame_modify)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_10)

        self.frame_37 = QFrame(self.frame_modify)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_19 = QLabel(self.frame_37)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_24.addWidget(self.label_19)

        self.ip_input_modify = QLineEdit(self.frame_37)
        self.ip_input_modify.setObjectName(u"ip_input_modify")
        self.ip_input_modify.setMaximumSize(QSize(140, 16777215))
        self.ip_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_24.addWidget(self.ip_input_modify)


        self.verticalLayout_19.addWidget(self.frame_37)

        self.line_11 = QFrame(self.frame_modify)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_11)

        self.frame_39 = QFrame(self.frame_modify)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.frame_39)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_26.addWidget(self.label_21)

        self.username_input_modify = QLineEdit(self.frame_39)
        self.username_input_modify.setObjectName(u"username_input_modify")
        self.username_input_modify.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_26.addWidget(self.username_input_modify)


        self.verticalLayout_19.addWidget(self.frame_39)

        self.line_12 = QFrame(self.frame_modify)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_12)

        self.frame_38 = QFrame(self.frame_modify)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_25.addWidget(self.label_20)

        self.password_input_modify = QLineEdit(self.frame_38)
        self.password_input_modify.setObjectName(u"password_input_modify")
        self.password_input_modify.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_25.addWidget(self.password_input_modify)


        self.verticalLayout_19.addWidget(self.frame_38)

        self.btn_modify_save = QPushButton(self.frame_modify)
        self.btn_modify_save.setObjectName(u"btn_modify_save")

        self.verticalLayout_19.addWidget(self.btn_modify_save)


        self.verticalLayout_20.addWidget(self.frame_modify)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)

        self.tabWidget.addTab(self.modify, "")

        self.verticalLayout_15.addWidget(self.tabWidget)


        self.verticalLayout_16.addWidget(self.groupBox_3)


        self.horizontalLayout_15.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.page_settings)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(200, 0))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_26)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_41 = QFrame(self.groupBox_4)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_23 = QLabel(self.frame_41)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_28.addWidget(self.label_23)

        self.comboBox_5 = QComboBox(self.frame_41)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_28.addWidget(self.comboBox_5)


        self.verticalLayout_22.addWidget(self.frame_41)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)


        self.verticalLayout_21.addWidget(self.groupBox_4)


        self.horizontalLayout_15.addWidget(self.frame_26)

        self.frame_32 = QFrame(self.page_settings)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(200, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_32)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.frame_27 = QFrame(self.page_settings)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(200, 0))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.frame_45 = QFrame(self.frame_3)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 30))
        self.frame_45.setMaximumSize(QSize(16777215, 30))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.log_label = QLabel(self.frame_45)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setFont(font)

        self.horizontalLayout_14.addWidget(self.log_label)


        self.verticalLayout_2.addWidget(self.frame_45)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dorsa_lbl.setText("")
        self.btn_side_playback.setText(QCoreApplication.translate("MainWindow", u"PlayBack", None))
        self.btn_side_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.btn_side_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_side_aboutus.setText(QCoreApplication.translate("MainWindow", u" About Us ", None))
        self.dorsa_lbl_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Train ID :", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.label_date_2.setText(QCoreApplication.translate("MainWindow", u"Selected Date :", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Speed : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.checkBox_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Server Name :", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.checkBox.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Train ID :", None))
        self.checkBox_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Start Date : ", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"End Date   : ", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start Time  : ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"End Time    : ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Train ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Station", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Start Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"End Date", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Start Time", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"End Time", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Download", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11BG65", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Esfahan", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1403/05/11", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1403/05/18", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"12:25:41", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"08:59:59", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Manage Systems", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name  : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"City : ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"IP Address : (192.168.1.1)", None))
        self.ip_input.setText(QCoreApplication.translate("MainWindow", u"192.168.1.1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.btn_add_check_connection.setText(QCoreApplication.translate("MainWindow", u"Check Connection", None))
        self.btn_save_add.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_system_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_system_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name  : ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"City : ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"IP Address : ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.btn_modify_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modify), QCoreApplication.translate("MainWindow", u"Modify", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Language : ", None))
        self.log_label.setText("")
    # retranslateUi

