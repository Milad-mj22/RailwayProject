import sys
import os
import shutil
from PySide6.QtCore import QThread, Signal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QLabel, QFileDialog
import subprocess
import time
import platform



class ShareCopyWorker(QThread):
    progress = Signal(int)
    log = Signal(str)
    completed = Signal()
    error = Signal(str)

    def __init__(self, src_path, dst_path, conn_details):
        super().__init__()
        self.src_path = src_path
        self.dst_path = dst_path
        self.conn_details = conn_details

        # Variables
        self.network_path = conn_details['share']
        self.drive_letter = "Z:"
        self.username = conn_details['username']
        self.password = conn_details['password']
        self.folder_to_copy = src_path
        self.destination_folder = dst_path


    def run(self):

        try:
            self.log.emit("Checking if drive is mapped...")
            if not self.is_drive_mapped():
                self.log.emit("Mapping network drive...")
                self.map_network_drive()

            if os.path.exists(self.drive_letter):
                self.log.emit("Creating destination folder if it does not exist...")
                if not os.path.exists(self.destination_folder):
                    os.makedirs(self.destination_folder)

                destination_path = os.path.join(self.destination_folder, os.path.basename(self.folder_to_copy))
                if os.path.exists(destination_path):
                    self.log.emit("Removing existing destination folder...")
                    shutil.rmtree(destination_path)

                total_size = self.get_folder_size(self.folder_to_copy)
                copied_size = 0

                self.log.emit("Starting copy...")

                self.start_time = time.time()
                print('1')
                for root, dirs, files in os.walk(self.folder_to_copy):
                    dest_dir = os.path.join(destination_path, os.path.relpath(root, self.folder_to_copy))
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)

                    for file in files:
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(dest_dir, file)
                        copied_size += os.path.getsize(src_file)
                        shutil.move(src_file, dest_file)

                        progress = int(copied_size / total_size * 100)
                        self.progress.emit(progress)
                        self.log.emit("Starting copy...   {}".format(str(file)))
                        print(file)


                self.completed.emit()
                self.end_time = time.time()
                self.log.emit("Copy completed! Elpassed Time :{}".format(self.end_time-self.start_time))
            else:
                raise Exception('Failed to map the network drive. Check your network path, username, and password.')

        except Exception as e:
            print(str(e))
            self.error.emit(str(e))

        finally:
            self.disconnect_network_drive()

    def get_folder_size(self, folder):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def map_network_drive(self):
        command = f'net use {self.drive_letter} {self.network_path} /user:{self.username} {self.password}'
        os.system(command)

    def disconnect_network_drive(self):
        os.system(f'net use {self.drive_letter} /delete')

    def is_drive_mapped(self):
        try:
            output = subprocess.check_output(f'net use {self.drive_letter}', shell=True, stderr=subprocess.STDOUT).decode()
            return self.network_path in output
        except subprocess.CalledProcessError:
            return False
