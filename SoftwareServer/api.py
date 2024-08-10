
from database import DataBase
from main_ui import UI_main_window_org
import platform,subprocess
from get_ping import PingThread
import threading
from PySide6.QtWidgets import QMessageBox



class API:
    def __init__(self, ui_obj:UI_main_window_org):

        self.ui_obj = ui_obj
        self.create_db_obj()
        self.load_base_parms()
        self.button_connector()
        self.name_last_select_modify = None


    def button_connector(self):

        self.ui_obj.btn_system_edit.clicked.connect(self.edit_system)
        self.ui_obj.btn_save_add.clicked.connect(self.add_system)
        self.ui_obj.btn_add_check_connection.clicked.connect(self.check_system_connection)
        self.ui_obj.btn_system_delete.clicked.connect(self.remove_system)



    def edit_system(self):

        select_name = self.ui_obj.get_combo_values(self.ui_obj.comboBox_systems)

        for system in self.system_datas:
            if select_name == system['name']:
                self.name_last_select_modify = select_name
                ret = self.load_system_config(system_name=system['name'])
                if ret:
                    self.ui_obj.set_modify_system(ret[0])


    def load_base_parms(self):
        names = self.load_system_names()
        print('names',names)
        if names is not None:
            self.ui_obj.show_systems(names)
        else:
            self.ui_obj.show_systems([])


        


    def create_db_obj(self):
        self.db = DataBase('data.db')

    def load_system_names(self):

        configs = self.db.fetch_table_as_dict(table_name='system_config')
        self.system_datas = configs
        names = []
        if len(configs)>=1:
            for config in configs:
                names.append(config['name'])
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





if __name__ == '__main__':

    obj = API('test')

    names = obj.load_system_names()
    print(names)
    configs = obj.load_system_config(names[0])
    print('configs',configs)