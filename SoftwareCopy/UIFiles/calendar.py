# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QFrame,
    QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_CalendarDialog(object):
    def setupUi(self, CalendarDialog):
        if not CalendarDialog.objectName():
            CalendarDialog.setObjectName(u"CalendarDialog")
        CalendarDialog.resize(354, 467)
        CalendarDialog.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.verticalLayout = QVBoxLayout(CalendarDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(CalendarDialog)
        self.GlobalStyleSheet.setObjectName(u"GlobalStyleSheet")
        self.GlobalStyleSheet.setStyleSheet(u"/**************************Global Font***************************/\n"
"\n"
"QWidget\n"
"{\n"
"    font: auto \"Roboto\";\n"
"    color: white; /* Ensuring text is visible on darker backgrounds */\n"
"}\n"
"\n"
"/***********************QCalendarWidget************************/\n"
"\n"
"QCalendarWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: transparent;\n"
"    color: rgb(220, 220, 220); \n"
"    font-size: 16pt;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    min-height: 40px;\n"
"    max-height: 40px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth\n"
"{\n"
"    background-color: transparent;\n"
"    min-height: 40px;\n"
"    max-height: 40px;\n"
"    min-width: 40px;\n"
"    max-width: 40px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #343a40; \n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth\n"
"{\n"
"    background-color: transparent;\n"
"    min-height: 40px;\n"
"    max-height: 40px;"
                        "\n"
"    min-width: 40px;\n"
"    max-width: 40px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #343a40;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth:hover,\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth:hover\n"
"{\n"
"    background-color: #343a40; \n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth:pressed,\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth:pressed\n"
"{\n"
"    background-color: #23272b; \n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar \n"
"{\n"
"    background-color: transparent; \n"
"    min-height: 80px;\n"
"}\n"
"\n"
"QCalendarWidget QTableView \n"
"{\n"
"    outline: none;\n"
"    background-color: rgba(10, 14, 26, 255); \n"
"    selection-background-color: #7892DF;\n"
"    selection-color: white;\n"
"	alternate-background-color: transparent;\n"
"    border-top: 2px solid #343a40;\n"
"    border-bottom: 2px solid #343a40;\n"
"}\n"
"\n"
"QCalendarWidget QComboBox QAbstractItemView {\n"
"    background-color: red; /* "
                        "Background color of the dropdown items */\n"
"    selection-background-color: red; /* Background color of a selected item */\n"
"    selection-color: red; /* Text color of a selected item */\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LocalStyleSheet = QWidget(self.GlobalStyleSheet)
        self.LocalStyleSheet.setObjectName(u"LocalStyleSheet")
        self.verticalLayout_3 = QVBoxLayout(self.LocalStyleSheet)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PointStyleSheet = QWidget(self.LocalStyleSheet)
        self.PointStyleSheet.setObjectName(u"PointStyleSheet")
        self.PointStyleSheet.setStyleSheet(u"/*******************PmainFrameStyle********************/\n"
"\n"
"*[styleSheet=\"PmainFrameStyle\"]\n"
"{\n"
"	background-color: rgba(10, 14, 26, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/*******************PokPushButtonStyle********************/\n"
"\n"
"*[styleSheet=\"PokPushButtonStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(126, 132, 162), stop:1 rgb(31, 42, 77));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 12px;\n"
"	min-width: 150;\n"
"	max-width: 150;\n"
"	min-height:40;\n"
"	max-height: 40;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"PokPushButtonStyle\"]:disabled\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(189, 189, 191, 255), stop:1 rgba(189, 189, 191, 255));\n"
"	color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"*[styleSheet=\"PokPushButtonStyle\"]:hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x"
                        "2:1, y2:0.477, stop:0 rgb(139, 146, 179), stop:1 rgba(40, 67, 98, 219));\n"
"}\n"
"\n"
"*[styleSheet=\"PokPushButtonStyle\"]:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"/*******************PcancelPushButtonStyle********************/\n"
"\n"
"*[styleSheet=\"PcancelPushButtonStyle\"]\n"
"{\n"
"	border: 2px solid  rgb(126, 132, 162);\n"
"	color:  rgb(126, 132, 162);\n"
"	border-radius: 12px;\n"
"	min-width: 150;\n"
"	max-width: 150;\n"
"	min-height: 36;\n"
"	max-height: 36;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"PcancelPushButtonStyle\"]:disabled\n"
"{\n"
"	border: 2px solid rgba(189, 189, 191, 255);\n"
"	color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"*[styleSheet=\"PcancelPushButtonStyle\"]:hover\n"
"{\n"
"	border: 2px solid rgb(139, 146, 179);\n"
"	color:  rgb(139, 146, 179);\n"
"}\n"
"\n"
"*[styleSheet=\"PcancelPushButtonStyle\"]:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.PointStyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"PmainFrameStyle")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 17)
        self.calendar = QCalendarWidget(self.main_frame)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setMaximumSize(QSize(350, 16777215))
        self.calendar.setFirstDayOfWeek(Qt.Sunday)
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)

        self.verticalLayout_5.addWidget(self.calendar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.main_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setEnabled(True)
        self.cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_btn.setStyleSheet(u"PcancelPushButtonStyle")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.ok_btn = QPushButton(self.main_frame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setEnabled(True)
        self.ok_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ok_btn.setStyleSheet(u"PokPushButtonStyle")

        self.horizontalLayout.addWidget(self.ok_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.main_frame)


        self.verticalLayout_3.addWidget(self.PointStyleSheet)


        self.verticalLayout_2.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(CalendarDialog)

        QMetaObject.connectSlotsByName(CalendarDialog)
    # setupUi

    def retranslateUi(self, CalendarDialog):
        CalendarDialog.setWindowTitle(QCoreApplication.translate("CalendarDialog", u"Dialog", None))
        self.cancel_btn.setText(QCoreApplication.translate("CalendarDialog", u"Cancel", None))
        self.ok_btn.setText(QCoreApplication.translate("CalendarDialog", u"OK", None))
    # retranslateUi

