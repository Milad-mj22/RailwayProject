import sys
import subprocess
import platform
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject

import threading
class PingThread(QObject):
    # Define a signal that will be emitted when a ping result is ready
    ping_result = Signal(str)

    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def run(self):
        """Ping an IP address and emit the result."""
        try:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, "4", self.ip]
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if output.returncode == 0:
                result = f"Ping to {self.ip} successful:\n{output.stdout}"
                
            else:
                result = f"Ping to {self.ip} failed!\n{output.stderr}"
        except Exception as e:
            result = f"Ping to {self.ip} failed due to an exception: {str(e)}"
        
        self.ping_result.emit(result)