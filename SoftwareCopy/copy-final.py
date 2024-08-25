import sys
import os
import shutil
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QLabel, QFileDialog
import subprocess
import time

class ShareCopyWorker(QThread):
    progress = pyqtSignal(int)
    completed = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, src_path, dst_path, conn_details):
        super().__init__()
        self.src_path = src_path
        self.dst_path = dst_path
        self.conn_details = conn_details

        # Variables
        self.network_path = r"\\192.168.1.14\share"  # Path to the shared folder
        self.drive_letter = "Z:"  # Drive letter to map the network share to
        self.username = "PC"  # Username for the Windows 7 PC
        self.password = "1"  # Password for the Windows 7 PC
        self.folder_to_copy = r"\\192.168.1.14\share"  # Path to the file you want to copy
        self.destination_folder = r"asd"  # Destination folder on the shared drive

    def run(self):
        try:
            # Ensure the drive is mapped
            if not self.is_drive_mapped():
                self.map_network_drive()

            # Check if the drive is successfully mapped
            if os.path.exists(self.drive_letter):
                # Create destination folder if it does not exist
                if not os.path.exists(self.destination_folder):
                    os.makedirs(self.destination_folder)

                # Copy the folder
                destination_path = os.path.join(self.destination_folder, os.path.basename(self.folder_to_copy))
                if os.path.exists(destination_path):
                    shutil.rmtree(destination_path)  # Remove the destination folder if it already exists

                total_size = self.get_folder_size(self.folder_to_copy)
                copied_size = 0

                for root, dirs, files in os.walk(self.folder_to_copy):
                    dest_dir = os.path.join(destination_path, os.path.relpath(root, self.folder_to_copy))
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)

                    for file in files:
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(dest_dir, file)
                        shutil.copy2(src_file, dest_file)
                        copied_size += os.path.getsize(src_file)
                        progress = int(copied_size / total_size * 100)
                        self.progress.emit(progress)

                self.completed.emit()
            else:
                raise Exception('Failed to map the network drive. Check your network path, username, and password.')

        except Exception as e:
            self.error.emit(str(e))

        finally:
            # Optionally disconnect the network drive after copying the folder
            self.disconnect_network_drive()

    def get_folder_size(self, folder):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    # Function to map network drive
    def map_network_drive(self):
        command = f'net use {self.drive_letter} {self.network_path} /user:{self.username} {self.password}'
        os.system(command)

    # Function to disconnect network drive
    def disconnect_network_drive(self):
        os.system(f'net use {self.drive_letter} /delete')

    # Function to check if drive is mapped
    def is_drive_mapped(self):
        try:
            output = subprocess.check_output(f'net use {self.drive_letter}', shell=True, stderr=subprocess.STDOUT).decode()
            return self.network_path in output
        except subprocess.CalledProcessError:
            return False

class CopyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Folder Copy from Share')

        layout = QVBoxLayout()

        self.ip_label = QLabel('Enter IP address:')
        self.ip_input = QLineEdit(self)

        self.username_label = QLabel('Enter Username:')
        self.username_input = QLineEdit(self)

        self.password_label = QLabel('Enter Password:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.src_label = QLabel('Source Folder:')
        self.src_input = QLineEdit(self)
        self.src_browse_button = QPushButton('Browse', self)
        self.src_browse_button.clicked.connect(self.browse_src_folder)

        self.dst_label = QLabel('Destination Folder:')
        self.dst_input = QLineEdit(self)
        self.dst_browse_button = QPushButton('Browse', self)
        self.dst_browse_button.clicked.connect(self.browse_dst_folder)

        self.copy_button = QPushButton('Start Copy', self)
        self.copy_button.clicked.connect(self.start_copy)

        self.progress_bar = QProgressBar(self)

        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.src_label)
        layout.addWidget(self.src_input)
        layout.addWidget(self.src_browse_button)
        layout.addWidget(self.dst_label)
        layout.addWidget(self.dst_input)
        layout.addWidget(self.dst_browse_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def browse_src_folder(self):
        src_path = QFileDialog.getExistingDirectory(self, 'Select Source Folder')
        if src_path:
            self.src_input.setText(src_path)

    def browse_dst_folder(self):
        dst_path = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')
        if dst_path:
            self.dst_input.setText(dst_path)

    def start_copy(self):
        ip = self.ip_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        src_path = self.src_input.text()
        dst_path = self.dst_input.text()

        # if ip and username and password and src_path and dst_path:
        conn_details = {
            'ip': ip,
            'username': username,
            'password': password,
            'share': src_path.split('\\')[0]
        }
        self.worker = ShareCopyWorker(src_path, dst_path, conn_details)
        self.worker.progress.connect(self.update_progress)
        self.worker.completed.connect(self.copy_completed)
        self.worker.error.connect(self.show_error)
        self.worker.start()
        # else:
        #     self.progress_bar.setFormat("Please fill all fields.")

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def copy_completed(self):
        self.progress_bar.setValue(100)
        self.progress_bar.setFormat("Copy Completed!")

    def show_error(self, error):
        self.progress_bar.setFormat(f"Error: {error}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CopyApp()
    ex.show()
    sys.exit(app.exec_())
