import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtGui import QAction, QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Custom Toolbar Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a toolbar
        toolbar = QToolBar("My Toolbar", self)
        toolbar.setMovable(False)  # Make the toolbar fixed (not movable)
        self.addToolBar(toolbar)

        # Customize the toolbar style
        toolbar.setStyleSheet("""
            QToolBar {
                background-color: #1e1e1e;  /* Dark background like Windows 10 */
                spacing: 10px;  /* Spacing between items */
                padding: 5px;   /* Padding around the toolbar */
            }
            QToolButton {
                color: white;  /* White text color for the toolbar buttons */
                font-size: 14px;  /* Font size */
                background-color: #1e1e1e;  /* Dark background for buttons */
                border: none;  /* No border */
                padding: 5px;  /* Padding inside the buttons */
            }
            QToolButton:hover {
                background-color: #2a2a2a;  /* Lighter background on hover */
            }
            QToolButton:pressed {
                background-color: #3a3a3a;  /* Even lighter background on press */
            }
        """)

        # Add actions (buttons) to the toolbar
        action1 = QAction(QIcon("path/to/icon1.png"), "Button 1", self)
        action2 = QAction(QIcon("path/to/icon2.png"), "Button 2", self)
        action3 = QAction(QIcon("path/to/icon3.png"), "Button 3", self)

        toolbar.addAction(action1)
        toolbar.addAction(action2)
        toolbar.addAction(action3)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
