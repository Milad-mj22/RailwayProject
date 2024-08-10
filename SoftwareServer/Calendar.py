import time
import datetime

import re
import cv2
#from persiantools.jdatetime import JalaliDateTime, JalaliDate
from datetime import datetime, date

from PySide6.QtWidgets import QApplication, QToolButton
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox, QGridLayout, QLabel, QDialog,QDialogButtonBox,QPushButton

from guiBackend import GUIBackend
from UIFiles.calendar import Ui_CalendarDialog
from PySide6.QtCore import QDate
from PySide6 import QtCore as sQtCore

from persiantools.jdatetime import JalaliDateTime
import jdatetime


DAY_BUTTON_STYLE = """QPushButton {

    background-color:transparent;
}

QPushButton:hover {
    background-color:rgba(0,0,255,50);
}
"""

DAY_BUTTON_SELECTED_STYLE = """

QPushButton {
    border:2px solid red;
    color: rgb(0,64,64);
    border-radius:3px;
    background-color:transparent;
}
"""


MAIN_STYLE = """
QComboBox
{
	border:2px solid #e0e0e0;
    border-radius: 17px;
    padding: 1px 8px 1px 8px;
	min-height: 20px;
	font-size: 14px;
}

QComboBox::drop-down
{
    background-color: transparent;
	border-top-right-radius: 8px;
	border-bottom-right-radius: 8px;
}

QDialogButtonBox{
color:red;
}
"""

        



class JalaliCalendarDialog(QWidget):
   
    def __init__(self, input_field: QtWidgets.QLineEdit, date=None,maimumwidth:int = 280,maximumheight:int = 150):
        super().__init__()

        self.setWindowTitle("Jalali Calendar Dialog")


        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None

        self.selected_day = None
        self.input_field = input_field

        if date is None:
            date = JalaliDateTime.now()
        


        self.date:datetime = date

        # Set up the layout
        layout = QVBoxLayout()


        self.yearCombo = QComboBox()
        self.monthCombo = QComboBox()

        # Add years to the year combo box
        current_jalali_year = JalaliDateTime.now().year
        for year in range(current_jalali_year - 50, current_jalali_year + 50):
            self.yearCombo.addItem(str(year))

        # Add months to the month combo box
        jalali_months = [
            "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
        ]
        for month in jalali_months:
            self.monthCombo.addItem(month)

        self.yearCombo.setCurrentText(str(current_jalali_year))
        self.monthCombo.setCurrentIndex(JalaliDateTime.now().month - 1)

        self.yearCombo.currentTextChanged.connect(self.updateCalendar)
        self.monthCombo.currentIndexChanged.connect(self.updateCalendar)

        self.calendarGrid = QGridLayout()
        self.selected_button = None
        self.updateCalendar()

        layout.addWidget(self.yearCombo)
        layout.addWidget(self.monthCombo)

        calendar_widget = QWidget()
        calendar_widget.setLayout(self.calendarGrid)
        layout.addWidget(calendar_widget)

        # Add buttons
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.selected_date)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

        self.setLayout(layout)
        self.setStyleSheet(MAIN_STYLE)

        self.__set_date_into_field()
        # self.show()

        calendar_widget.setMaximumWidth(maimumwidth)
        calendar_widget.setMaximumHeight(maximumheight)



    def reject(self):
        self.close()

    def updateCalendar(self):
        # Clear previous widgets in the calendar grid
        while self.calendarGrid.count():
            item = self.calendarGrid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        year = int(self.yearCombo.currentText())
        month = self.monthCombo.currentIndex() + 1

        first_day_of_month = JalaliDateTime(year, month, 1)
        first_day_of_week = first_day_of_month.weekday()

        days_in_month = self.days_in_jalali_month(year, month)

        day = 1
        for week in range(6):
            for weekday in range(7):
                if week == 0 and weekday < first_day_of_week:
                    label = QLabel("")
                    self.calendarGrid.addWidget(label, week, weekday)
                elif day > days_in_month:
                    label = QLabel("")
                    self.calendarGrid.addWidget(label, week, weekday)
                else:
                    button = QPushButton(str(day))
                    GUIBackend.set_style(button, DAY_BUTTON_STYLE)
                    # button.setStyleSheet(DAY_BUTTON_STYLE)

                    self.calendarGrid.addWidget(button, week, weekday)
                    button.clicked.connect(self.select_day)
                    button.clicked.connect(self.selected_date)

                    # self.select_day()

                    day += 1

                    

        # self.calendarGrid.setLayout(layout)

        # self.calendarGrid.setLayout(layout)

    @staticmethod
    def days_in_jalali_month(year, month):
        if month <= 6:
            return 31
        elif month <= 11:
            return 30
        else:
            # Check for leap year
            return 30 if JalaliDateTime.is_leap(year) else 29


    def select_day(self):
        try:
            if self.selected_button:
                GUIBackend.set_style(self.selected_button, DAY_BUTTON_STYLE)
        except RuntimeError as e:
            print("Button has been deleted.")
        self.selected_button = self.sender()
        self.selected_day = int(self.selected_button.text())
        GUIBackend.set_style(self.selected_button, DAY_BUTTON_SELECTED_STYLE)

    def selected_date(self):
        year = int(self.yearCombo.currentText())
        month = self.monthCombo.currentIndex() + 1
        day = self.selected_day
        

        if day:
            self.date = JalaliDateTime(year, month, day)
            self.__set_date_into_field()



        # return JalaliDateTime(year, month, day) if day else None
    
    def __set_date_into_field(self,):
        str_date = self.date.strftime("%Y/%m/%d")
        self.input_field.setText(str_date)
        # GUIBackend.set_input(self.input_field, str_date)





if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication as sQApplication

    app = sQApplication()
    win = JalaliCalendarDialog()

    win.show()

    import sys
    sys.exit(app.exec())