import os
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'main_UI.ui'), os.path.join('UIFiles', 'main_UI.py')))
os.system('CMD /C pyside6-rcc assets.qrc -o assets.py')#PySide
##############################################################################################################################

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox, QGridLayout, QLabel, QDialog,QDialogButtonBox,QPushButton,QFrame
import sqlite3
import sys,os,platform,time,subprocess,threading
from database import DataBase
from copy_ping import ShareCopyWorker
from persiantools.jdatetime import JalaliDateTime
import jdatetime
from Calendar import  JalaliCalendarDialog
from guiBackend import GUIBackend
from PySide6.QtCore import QTimer
from login import LoginPage
from PySide6.QtCore import Qt
from UIFiles.main_UI import Ui_MainWindow

from PySide6.QtWidgets import QGraphicsBlurEffect
from PySide6.QtGui import QFont,QIcon
from CustomTitle import CustomTitleBar
from timeLine import TimelineSlider

import assets

from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QEvent


from constanst import ONE_HOUR


# ui class
class UI_main_window_org(sQMainWindow, Ui_MainWindow):
    global widgets
    # widgets = Ui_MainWindow

    def __init__(self):
        super(UI_main_window_org, self).__init__()
        self.setWindowTitle("Sepanta RailWay Monitoring")

        # window setup
        self.setupUi(self)
        self.setWindowTitle("Iran RailWay Monitoring")
        # Set the window icon
        self.setWindowIcon(QIcon(":/icons/icons/download.png"))


        
        self.stackedWidget.setCurrentWidget(self.page_playback)
        



        self.button_connector()
        
        # Create a central widget
        central_widget = self.calendar_widget
        self.calendar_dialog = JalaliCalendarDialog(self.label_date)
        self.calendar_dialog.setParent(central_widget)



        # timeline_widget = self.layout_timeline
        self.timeline = TimelineSlider(duration_ms=ONE_HOUR,played_color="green", unplayed_color="green",
                                     played_red_color="red", unplayed_red_color="red",
                                     show_dividers=False, groove_height=25,time_label=self.time_label)


        self.timeline.set_minutes_segments([])
        # GUIBackend.add_widget(self.frame_timeline,self.timeline)
        GUIBackend.add_widget(self.layout_timeline,self.timeline)



        self.preview_login = False



        # Create animations
        self.animation = QPropertyAnimation(self.toggle_frame, b"geometry")
        self.animation.setDuration(1500)  # Duration in milliseconds (1.5 seconds)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # Easing curve for smooth animation

        # Connect the button's clicked event
        self.btn_logo.clicked.connect(self.toggle_frame_visibility)
        self.btn_logo.installEventFilter(self)  # Install an event filter to handle double clicks

    def toggle_frame_visibility(self):
        if self.toggle_frame.isVisible():
            # Animate closing
            self.animation.setStartValue(self.toggle_frame.geometry())
            self.animation.setEndValue(QRect(self.toggle_frame.x(), self.toggle_frame.y(), 0, self.toggle_frame.height()))
            self.animation.start()
            self.toggle_frame.setVisible(False)
        else:
            # Animate opening
            self.toggle_frame.setVisible(True)
            self.animation.setStartValue(QRect(self.toggle_frame.x(), self.toggle_frame.y(), 0, self.toggle_frame.height()))
            self.animation.setEndValue(QRect(self.toggle_frame.x(), self.toggle_frame.y(), 200, self.toggle_frame.height()))
            self.animation.start()

    def eventFilter(self, source, event):
        if source == self.btn_logo and event.type() == QEvent.MouseButtonDblClick:
            # Hide frame on double click with animation
            if self.toggle_frame.isVisible():
                self.animation.setStartValue(self.toggle_frame.geometry())
                self.animation.setEndValue(QRect(self.toggle_frame.x(), self.toggle_frame.y(), 0, self.toggle_frame.height()))
                self.animation.start()
                self.toggle_frame.setVisible(False)
            return True
        return super(UI_main_window_org, self).eventFilter(source, event)


    def open_calender(self, name:str):
        
        self.calenders[name].show()

    def button_connector(self):

        self.btn_side_playback.clicked.connect(self.set_stack_widget)
        self.btn_side_download.clicked.connect(self.set_stack_widget)
        self.btn_side_settings.clicked.connect(self.set_stack_widget)
        self.btn_side_aboutus.clicked.connect(self.set_stack_widget)


        



    def show_login(self):
        if not  self.preview_login:
            self.applyBlurEffect()
            self.login_ui = LoginPage(self)
            self.login_ui.show()
            self.preview_login = True
            self.login_ui.open_button.clicked.connect(self.check_password)
            self.login_ui.close_button.clicked.connect(self.close_login)

    def close_login(self):
            self.preview_login = False

    def check_password(self):

        password = self.login_ui.password
        self.preview_login = False
        if password != '':
            res = self.db.fetch_table_as_dict(table_name='password')
            if len(res)==1:
                res = res[0]
                if str(password) == str(res['password']):
                    self.login_ui.close()
                    self.update_log('Login Succussfully')
                    self.show_timeline(mode=True)

                else:
                    self.show_error('Password is Wrong')

    def time_line_copy(self):
        self.show_timeline(mode=False)

        if  self.start_date.text() !='' and  self.end_date.text() !='':

            start_time={}
            get_time = self.timeEdit_start.time()
            h = get_time.hour()
            m = get_time.minute()
            

            get_date = self.start_date.text().split('/')

            start_time = JalaliDateTime.now()
            start_time = start_time.replace(year=int(get_date[0]),month=int(get_date[1]),day = int(get_date[2]), hour=h,minute=m)
            print(start_time)


            get_time = self.timeEdit_end.time()
            h = get_time.hour()
            m = get_time.minute()

            get_date = self.end_date.text().split('/')


            end_time = JalaliDateTime.now()
            end_time = end_time.replace(year=int(get_date[0]),month=int(get_date[1]),day = int(get_date[2]), hour=h,minute=m)

            print(end_time)

            if end_time<start_time:
                print('End time should be bigger than start time')
                self.show_error('End time should be bigger than start time')



    def covert_date(self,jdatetime):
        date = jdatetime.strftime('%Y/%m/%d')
        return date
    
    def set_stack_widget(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_side_playback":
            self.stackedWidget.setCurrentWidget(self.page_playback)
        if btnName == "btn_side_download":
            self.stackedWidget.setCurrentWidget(self.page_download)
        if btnName == "btn_side_settings":
            self.stackedWidget.setCurrentWidget(self.page_settings)
        if btnName == "btn_side_aboutus":
            self.stackedWidget.setCurrentWidget(self.page_playback)


    def close_win(self):
        self.close()
        # pid = os.getpid()
        # os.kill(pid, SIGKILL)
        sys.exit()

    def minimize_win(self):
        self.showMinimized()



    def load_fields(self):
        res = self.db.fetch_table_as_dict()
        if len(res)==1:
            res = res[0]
            self.ip_input.setText(res['ip'])
            self.username_input.setText(res['username'])
            self.password_input.setText(res['password'])

    


    def save_ip(self):
        self.db.update_row_by_id_zero(column_name='ip',new_value=self.ip_input.text())
    def save_username(self):
        self.db.update_row_by_id_zero(column_name='username',new_value=self.username_input.text())
    def save_password(self):
        self.db.update_row_by_id_zero(column_name='password',new_value=self.password_input.text())

    def load_pathes(self):
        res = self.db.fetch_table_as_dict(table_name='pathes')
        if len(res)==1:
            res = res[0]
            self.src_path = res['folder_to_copy']
            self.dst_path = res['destination_folder']


    def start_copy(self):
        ip = self.ip_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        src_path = self.src_path
        dst_path = self.dst_path

        # if ip and username and password and src_path and dst_path:
        if self.ping_host(ip):
            conn_details = {
                'ip': ip,
                'username': username,
                'password': password,
                'share': src_path
            }
            self.worker = ShareCopyWorker(src_path, dst_path, conn_details)
            self.worker.progress.connect(self.update_progress)
            self.worker.log.connect(self.update_log)
            self.worker.completed.connect(self.copy_completed)
            self.worker.error.connect(self.show_error)
            self.worker.start()
            # self.worker.run()
        else:
            self.show_error("Ping failed. Check the IP address and try again.")
        # else:
        #     self.log_label.setText("Please fill all fields.")

    def ping_host(self, ip):

        try:
            # Determine the ping command based on the OS
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, "1", ip]
            
            # Run the command
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if output.returncode == 0:
                self.update_log('1 packets transmitted, 1 packets received')
                return True
            # Display the result
            # if output.returncode == 0:
            #     self.result_area.setPlainText(f"Ping to {ip_address} successful!\n{output.stdout}")
            else:
                self.update_log(f"Ping to {ip} failed!\n{output.stderr}")

                return False
        except Exception as e:
            self.update_log(f"Ping to {ip} failed!\n{output.stderr}")

            return False


    def update_progress(self, value):
        print(value)
        self.progress_bar.setValue(value)

    def update_log(self, message):
        self.log_label.setText(message)
        QTimer.singleShot(3000, lambda: self.show_error(''))

    def copy_completed(self):
        self.progress_bar.setValue(100)
        self.log_label.setText("Copy Completed!")
        # threading.Timer(3,self.update_log,args=('',)).start()
        # threading.Timer(3,self.update_progress,args=(0,)).start()


    def show_error(self, error):
        if error !='':
            self.log_label.setText(f"Error: {error}")
        else:
            self.log_label.setText('')

        QTimer.singleShot(3000, lambda: self.show_error(''))



    def show_timeline(self,mode):
        self.frame_date.setVisible(mode) 

        



    def applyBlurEffect(self):
        current_effect = self.graphicsEffect()
        if current_effect:
            self.setGraphicsEffect(None)
        else:
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)
            self.setGraphicsEffect(blur_effect)




    def show_systems(self,names):
        GUIBackend.set_combobox_items(self.comboBox_systems,[])
        GUIBackend.set_combobox_items(self.comboBox_systems,names)

    def get_combo_values(self,combo_name):

        name = GUIBackend.get_combobox_selected(combo_name)
        return name



    def get_add_system(self):
        input_fields = {}
        input_fields['name'] =GUIBackend.get_input_text(self.name_input)
        input_fields['ip'] =GUIBackend.get_input_text(self.ip_input)
        input_fields['username'] = GUIBackend.get_input_text(self.username_input)
        input_fields['password'] =GUIBackend.get_input_text(self.password_input)
        input_fields['city'] =GUIBackend.get_input_text(self.city_input)

        for field in input_fields:
            if input_fields[field] == '':
                self.show_error('Field {} Must be have value'.format(field))
                return None


        return input_fields


    def get_add_ip(self):

        input_fields = {}
        input_fields['ip'] =GUIBackend.get_input_text(self.ip_input)
        return input_fields



    def append_ping_result(self, result):
        """Append the ping result to the QTextEdit."""
        # print(result)
        self.textEdit_ping_status.append(result)
    def clear_ping_result(self):
        self.textEdit_ping_status.setText('')





    def set_modify_system(self,values):

        GUIBackend.set_input(self.name_input_modify,values['name'])
        GUIBackend.set_input(self.ip_input_modify,values['ip'])
        GUIBackend.set_input(self.username_input_modify,values['username'])
        GUIBackend.set_input(self.password_input_modify,values['password'])
        GUIBackend.set_input(self.city_input_modify,values['city'])









    def set_item_combo_box(self,combo_name,items):

        GUIBackend.set_combobox_items(combo_name,items)
  

    def ret_current_value_combo_box(self,combo_name):
        return combo_name.currentText()
        


    def update_image(self, pixmap):
        # Resize the image to fit the label
        # self.show_image.setPixmap(pixmap.scaled(self.show_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.show_image.setPixmap(pixmap.scaled(self.show_image.size()))#, Qt.KeepAspectRatio, Qt.SmoothTransformation))







if __name__ == "__main__":



    from api import API
    app = sQApplication()

    win = UI_main_window_org()
    api = API(win)
    win.show()
    sys.exit(app.exec())