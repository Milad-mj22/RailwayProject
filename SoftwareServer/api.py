
from database import DataBase
from main_ui import UI_main_window_org
import platform,subprocess
from get_ping import PingThread
import threading
from PySide6.QtWidgets import QMessageBox
from constanst import MAX_SPEED,COLUMN_DESTINATION,TABLE_PATHES
import os
from loading_train import LoadingWindow
from ImageLoader import ImageLoader
from threading import Thread, Event

class API:
    def __init__(self, ui_obj:UI_main_window_org):

        self.ui_obj = ui_obj
        self.create_db_obj()
        self.load_base_parms()
        self.button_connector()
        self.name_last_select_modify = None
        self.speed_rate = 1
        self.check_available_trains()
        self.train_id_selected = False

        self.stop_event = Event()
        self.image_loader = ImageLoader(self.stop_event,'', self.speed_rate)



    def button_connector(self):

        self.ui_obj.btn_system_edit.clicked.connect(self.edit_system)
        self.ui_obj.btn_save_add.clicked.connect(self.add_system)
        self.ui_obj.btn_add_check_connection.clicked.connect(self.check_system_connection)
        self.ui_obj.btn_system_delete.clicked.connect(self.remove_system)

        self.ui_obj.speed_btn.clicked.connect(self.set_speed)
        self.ui_obj.btn_side_download.clicked.connect(self.load_download_base_params)

        self.ui_obj.btn_add.clicked.connect(self.add_name)
        self.ui_obj.btn_remove.clicked.connect(self.remove_name)
        self.ui_obj.refresh_btn.clicked.connect(self.check_available_trains)
        self.ui_obj.btn_select_train.clicked.connect(self.set_train_id)
        self.ui_obj.play_btn.clicked.connect(self.play_images)
        self.ui_obj.stop_btn.clicked.connect(self.stop_show_image)


    def edit_system(self):

        select_name = self.ui_obj.get_combo_values(self.ui_obj.comboBox_systems)

        for system in self.system_datas:
            if select_name == system['name']:
                self.name_last_select_modify = select_name
                ret = self.load_system_config(system_name=system['name'])
                if ret:
                    self.ui_obj.set_modify_system(ret[0])


    def load_base_parms(self):
        names = self.load_system_spec_column(column_name='name')
        print('names',names)
        if names is not None:
            self.ui_obj.show_systems(names)
        else:
            self.ui_obj.show_systems([])


        


    def create_db_obj(self):
        self.db = DataBase('data.db')

    def load_system_spec_column(self,column_name):

        configs = self.db.fetch_table_as_dict(table_name='system_config')
        self.system_datas = configs
        names = []
        if len(configs)>=1:
            for config in configs:
                names.append(config[column_name])
        else:
            names=None
        return names


    def load_system_config(self,system_name):

        ret = self.db.fetch_spec_parm_table(table_name='system_config',col_name='name',spec_row=system_name)
        print('ret :',ret)
        return ret


    def add_system(self):

        input_fields = self.ui_obj.get_add_system()
        if input_fields != None:
            ret = self.db.add_value('system_config',**input_fields)
            if ret:
                self.ui_obj.update_log('New System ADD Successfully')
                self.load_base_parms()

            else:
                self.ui_obj.show_error('Cant Save New System')


    def check_system_connection(self):

        input_fields = self.ui_obj.get_add_ip()
        if input_fields['ip'] != None:
            ip = input_fields['ip']
            self.get_ping(ip = ip)



    def get_ping(self, ip):
        """Ping an IP address and return the result as a string."""
        self.ui_obj.clear_ping_result()
        self.ping_worker = PingThread(ip)
        self.ping_thread =  threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_worker.ping_result.connect(self.ui_obj.append_ping_result)
        self.ping_thread.start()



    def remove_system(self):

        select_name = self.ui_obj.get_combo_values(self.ui_obj.comboBox_systems)
        if select_name !='':
            # Show a confirmation dialog
            reply = QMessageBox.question(
                None, 'Confirm Deletion',
                f"Are you sure you want to delete the {select_name} ?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            # If the user clicks "Yes", proceed with the deletion
            if reply == QMessageBox.Yes:

                ret = self.db.remove_row_by_col_name(table_name='system_config',col_name='name',name_value=select_name)
                if ret:
                    self.ui_obj.update_log(f'Row {select_name} Reomved Successfully')
                    self.load_base_parms()
                else:
                    self.ui_obj.show_error(f'Cant Remove {select_name}')



    def set_speed(self):
        speed = self.ui_obj.speed_btn.text()
        speed = int(speed[:-1])
        speed = speed*2
        if speed> MAX_SPEED:
            speed = 1
        self.speed_rate = speed
        self.ui_obj.speed_btn.setText(str(speed)+'x')

        if self.image_loader is not None:
            self.image_loader.update_fps(speed_rate=self.speed_rate)









    def load_download_base_params(self):

        self.condidate_names = []

        self.download_systems_names = self.load_system_spec_column(column_name='name')
        self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all, items=self.download_systems_names)


    def add_name(self):

        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.combo_download_all)
        if text !='':
            self.download_systems_names.remove(text)

            self.condidate_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_selected,items=self.condidate_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all,items=self.download_systems_names)


    def remove_name(self):



        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.combo_download_selected)
        if text!='':
            self.condidate_names.remove(text)

            self.download_systems_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all,items=self.download_systems_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_selected,items=self.condidate_names)







    def get_main_path(self):


        des_path = self.db.fetch_table_as_dict(table_name=TABLE_PATHES)
        if des_path !=[]:
            self.des_path = des_path[0][COLUMN_DESTINATION]
            return self.des_path





    def check_available_trains(self):

        des_path =  self.get_main_path()
        self.des_path = des_path
        if des_path != '' or des_path !=[] or des_path is not None:
            trains = os.listdir(des_path)
            self.ui_obj.set_item_combo_box(self.ui_obj.combo_train_id,trains)


    def set_train_id(self):


        self.train_id = self.ui_obj.get_combo_values(self.ui_obj.combo_train_id)
        if self.train_id =='':
            print('Train id is none')
            return
        try:
            self.path_train_id = os.path.join(self.des_path,self.train_id)
        except:
            print('Error in get path train id not exist')
            return 


        days = self.get_days(train_path=self.path_train_id)
        print(days)

        self.ui_obj.calendar_dialog.set_spec_days(days)

        self.ui_obj.calendar_dialog.updateCalendar()
        

        self.loading = LoadingWindow(self.ui_obj)
        self.loading.show()


        self.train_id_selected = True
    




    def get_days(self,train_path):

        days = []
        if os.path.exists(train_path) and os.path.isdir(train_path):
            for year in os.listdir(train_path):
                year_path = os.path.join(train_path,year)
                if os.path.exists(year_path) and os.path.isdir(year_path):
                    for month in os.listdir(year_path):
                        month_path = os.path.join(year_path,month)
                        if os.path.exists(month_path) and os.path.isdir(month_path):
                            for day in os.listdir(month_path):
                                days.append(f'{year}_{month}_{day}')


                        else:
                            print(f"{month_path} is not a directory or does not exist.")
                else:
                    print(f"{year_path} is not a directory or does not exist.")
        else:
            print(f"{train_path} is not a directory or does not exist.")




        return days


    def play_images(self):

        if not self.image_loader.playing:

            if  self.image_loader.is_alive():
                text = 'Thread is already running.'
                print(text)
                self.ui_obj.show_error(text)
                return


            path_selected_day = self.get_path_selected_date()

                
            # Create a new Worker instance and start it
            self.stop_event.clear()  # Reset the stop event
            # self.image_loader = ImageLoader(self.stop_event)
            self.image_loader = ImageLoader(self.stop_event,path_selected_day, self.speed_rate)
            
            # ImageLoader runs in a separate thread
            self.image_loader.update_folder_path(path_selected_day)
            self.image_loader.image_signal.connect(self.ui_obj.update_image)  # Connect the signal to the update_image slot

            self.image_loader.start()
            
            text = 'Start Playing'
            self.ui_obj.update_log(text)


        else:
            text = 'First Stop Playing'
            print(text)
            self.ui_obj.show_error(text)


    def stop_show_image(self, event):
        # Stop the image loader thread when closing the window
        self.stop_event.set()
        self.image_loader.stop()
        text = 'Stop Playing'
        self.ui_obj.update_log(text)


  




    def get_path_selected_date(self):

        if not self.train_id_selected:
            print('First Set/Select train')
            return
        
        selected_date = self.ui_obj.calendar_dialog.str_date
        self.path_selected_day = os.path.join(self.des_path,self.train_id,selected_date)
        return self.path_selected_day









if __name__ == '__main__':

    obj = API('test')

    names = obj.load_system_names()
    print(names)
    configs = obj.load_system_config(names[0])
    print('configs',configs)