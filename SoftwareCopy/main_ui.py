
from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QApplication as sQApplication
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


from PySide6.QtWidgets import QGraphicsBlurEffect

# load ui file
ui_file = r'ui_copy.ui'
ui, _ = loadUiType(ui_file)






# ui class
class UI_main_window_org(sQMainWindow, ui):
    global widgets
    widgets = ui

    def __init__(self):
        super(UI_main_window_org, self).__init__()

        # window setup
        self.setupUi(self)
        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None
        self.show_timeline(mode=False) 
        self.stackedWidget.setCurrentWidget(self.copy)
        self.db = DataBase('data.db')
        self.button_connector()
        self.load_fields()
        self.load_pathes()

        

     

        self.calenders = {
            'start':JalaliCalendarDialog( self.start_date),
            'end'  :JalaliCalendarDialog(self.end_date)
        }
        self.calenders_btn = {
            'start': self.start_calendar_btn,
            'end': self.end_calendar_btn

        }
        for name , btn in self.calenders_btn.items():
            GUIBackend.button_connector_argument_pass(btn, self.open_calender, args=(name,))

        self.preview_login = False


    def open_calender(self, name:str):
        
        self.calenders[name].show()

    def button_connector(self):

        self.close_btn.clicked.connect(self.close_win)
        self.minimize_btn.clicked.connect(self.minimize_win)
        self.save_btn_ip.clicked.connect(self.save_ip)
        self.save_btn_username.clicked.connect(self.save_username)
        self.save_btn_password.clicked.connect(self.save_password)
        self.copy_button.clicked.connect(self.ui_copy)
        self.side_copy_btn.clicked.connect(self.set_stack_widget)
        self.side_profile_btn.clicked.connect(self.set_stack_widget)
        self.timeline_btn.clicked.connect(self.show_login)
        self.timeline_copy_btn.clicked.connect(self.time_line_copy)

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
            get_date = self.calenders['start'].date
            # get_date = get_date.jdate()
            get_time = self.timeEdit_end.time()
            h = get_time.hour()
            m = get_time.minute()

            start_time = get_date.replace(hour=h,minute=m)


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

            else:

                print('Start Doing Copy')

                self.image_condition = {'start':start_time,'end':end_time}
                self.start_copy(image_condition=self.image_condition)











    def covert_date(self,jdatetime):
        date = jdatetime.strftime('%Y/%m/%d')
        return date
    
    def set_stack_widget(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "side_copy_btn":
            self.stackedWidget.setCurrentWidget(self.copy)
        if btnName == "side_profile_btn":
            self.stackedWidget.setCurrentWidget(self.profile)


    def mousePressEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton and not self.isMaximized():
            # accept event only on top bar
            if (
                event.position().y() <= self.topFrame.height()
            ):
                self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPosition().toPoint()

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


    def ui_copy(self):

        self.show_timeline(mode=False) 
        self.start_copy()



    def start_copy(self,image_condition=None):
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
                'share': src_path,

            }
            self.worker = ShareCopyWorker(src_path, dst_path, conn_details,image_condition=image_condition)
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









if __name__ == "__main__":


    os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))


    app = sQApplication()
    win = UI_main_window_org()

    win.show()
    sys.exit(app.exec())