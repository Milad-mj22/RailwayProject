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


DAY_NOT_EXIST = 'RED'

DAY_BUTTON_STYLE = """QPushButton {

    background-color:transparent;
}

QPushButton:hover {
    background-color:rgba(0,0,255,50);
}
"""
DAY_BUTTON_SELECTED_STYLE = """

QPushButton {
    border:1px solid rgb(0,64,64);
    color: rgb(0,64,64);
    border-radius:3px;
    background-color:transparent;
}
"""

if DAY_NOT_EXIST=='RED':

    DAY_BUTTON_STYLE = """QPushButton {

        background-color:#ff4946;
    }

    QPushButton:hover {
        background-color:#902828;
    }
    """



    DAY_BUTTON_SELECTED_STYLE = """

    QPushButton {
        border:1px solid rgb(0,64,64);
        border-radius:3px;
        background-color:#902828;
    }
    """

DAY_BUTTON_EXIST_STYLE ="""QPushButton {

    background-color: #49ff46;
}

QPushButton:hover {
    background-color:#299028;
}
"""




DAY_BUTTON_SELECTED_EXIST_STYLE ="""
QPushButton {
    background-color: #299028;
    border:1px solid rgb(0,64,64);
    border-radius:3px;
}

"""





MAIN_STYLE = """
QComboBox {
    background-color: #3b4252;
	background-color: rgb(180, 180, 180);
    border: 1px solid #4c566a;
    border-radius: 5px;
    padding: 6px 10px;

	color: rgb(0, 0, 0);
}

QComboBox:hover {
    border: 1px solid #5e81ac;
}

QComboBox::drop-down {
    border: none;
}

QComboBox::down-arrow {
    image: url(:/icons/icons/icons8-drop-down-80.png);

    width: 12px;
    height: 12px;
}

QDialogButtonBox{
color:red;
}







QComboBox {
    background-color: #3b4252;
	background-color: rgb(180, 180, 180);
    border: 1px solid #4c566a;
    border-radius: 5px;
    padding: 6px 10px;

	color: rgb(0, 0, 0);
}

QComboBox:hover {
    border: 1px solid #5e81ac;
}

QComboBox::drop-down {
    border: none;
}

QComboBox::down-arrow {
    image: url(:/icons/icons/icons8-drop-down-80.png);

    width: 12px;
    height: 12px;
}


QPushButton{
	color: black;
    background-color:#0C356A;
	padding: 5px;
	font-size:12px;
	font-weight: bold;
	border-radius:7px;
	background-color: rgb(0, 17, 255);

}

QPushButton:hover{
	background-color: rgb(18, 3, 104);
}

QPushButton:disabled {
    color: #8D8D8D;
}

QPushButton:pressed {
	background: rgb(0, 0, 0);
}







"""

        



class JalaliCalendarDialog(QWidget):
   
    def __init__(self, input_field: QtWidgets, date=None,maimumwidth:int = 300,maximumheight:int = 180):
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
        self.spec_days = []
        self.path_selected_date = None
        self.parent_func = None

        if date is None:
            date = JalaliDateTime.now()
        


        self.date:datetime = date

        # Set up the layout
        layout = QVBoxLayout()


        self.yearCombo = QComboBox()
        self.monthCombo = QComboBox()

        # Add years to the year combo box
        current_jalali_year = JalaliDateTime.now().year
        for year in range(current_jalali_year -5, current_jalali_year +10):
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
        # buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonBox.accepted.connect(self.selected_date)
        # buttonBox.rejected.connect(self.reject)
        # layout.addWidget(buttonBox)

        self.setLayout(layout)
        self.setStyleSheet(MAIN_STYLE)

        self.__set_date_into_field()
        # self.show()

        calendar_widget.setMaximumWidth(maimumwidth)
        calendar_widget.setMaximumHeight(maximumheight)
        calendar_widget.setMinimumWidth(maimumwidth)
        calendar_widget.setMinimumHeight(maximumheight)



        self.yearCombo.setMaximumWidth(maimumwidth-20)
        self.yearCombo.setMinimumWidth(maimumwidth-20)
        self.monthCombo.setMinimumWidth(maimumwidth-20)
        self.monthCombo.setMaximumWidth(maimumwidth-20)



    def reject(self):
        self.close()

    def updateCalendar(self):
        self.path_selected_date = None
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

        self.btns_status = []

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


                    # self.select_day()



                    ######################3 milad add ##############
                    # if month<=9:
                    #     str_month = '0'+str(month)
                    # else:
                    #     str_month = month
                    # if day<=9:
                    #     str_day = '0'+str(day)
                    # else:
                    #     str_day = day

                    today = f'{year}_{month}_{day}'


                    if self.check_spec_day(day=today):
                        print(today)
                        try:
                            GUIBackend.set_style(button, DAY_BUTTON_EXIST_STYLE)
                            self.btns_status.append(True)
                            button.clicked.connect(self.select_day)
                            button.clicked.connect(self.selected_date)
                        except:
                            print('Error set date exist')
                            self.btns_status.append(False)

                            pass
                    
                    else:
                        GUIBackend.set_style(button, DAY_BUTTON_STYLE)

                        self.btns_status.append(False)



                    ############################################

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
                day = int(self.selected_button.text())
                if self.btns_status[day-1]:
                    GUIBackend.set_style(self.selected_button, DAY_BUTTON_EXIST_STYLE)
                else:
                    GUIBackend.set_style(self.selected_button, DAY_BUTTON_STYLE)



        except RuntimeError as e:
            print("Button has been deleted.")


        self.selected_button = self.sender()
        self.selected_day = int(self.selected_button.text())
        GUIBackend.set_style(self.selected_button, DAY_BUTTON_SELECTED_EXIST_STYLE)



    



    def selected_date(self):
        year = int(self.yearCombo.currentText())
        month = self.monthCombo.currentIndex() + 1
        day = self.selected_day
        



        if day:
            self.date = JalaliDateTime(year, month, day)
            self.__set_date_into_field()

        self.path_selected_date = f'{year}/{month}/{day}'

        # return JalaliDateTime(year, month, day) if day else None
    
    def __set_date_into_field(self,):
        str_date = self.date.strftime("%Y/%m/%d")
        self.str_date = str_date
        self.input_field.setText(str_date)

        if self.parent_func is not None:
            self.parent_func(self.date)

        # GUIBackend.set_input(self.input_field, str_date)



    def set_spec_days(self,spec_days):
        self.spec_days = spec_days




    def check_spec_day(self,day):
        if day in self.spec_days:
            return True
        return False




    def set_parent_function(self,func):
        self.parent_func = func






if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication as sQApplication

    app = sQApplication()
    win = JalaliCalendarDialog()

    win.show()

    import sys
    sys.exit(app.exec())