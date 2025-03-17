import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QClipboard

from ui_main import Ui_MainWindow

import mouse
import keyboard
import pyautogui

def get_color():
    x, y = mouse.get_position()
    rgb = pyautogui.screenshot().getpixel((x, y))
    return "#{:02X}{:02X}{:02X}".format(*rgb)

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        keyboard.add_hotkey('shift+f1', self.get_color)

        self.color_index = 0
        self.buttons: list[QPushButton] = [
            self.btn_color1,
            self.btn_color2,
            self.btn_color3,
        ]
        self.colors = {}
        self.button_connections = {}

    def get_color(self):
        color = get_color()
        self.colors[self.color_index] = color
        btn = self.buttons[self.color_index]

        btn.setStyleSheet(
            f'background: {color};'
            f'border-radius: 30px;'
            'border: 4px solid #5B67C3;'
        )

        if btn in self.button_connections:
            old_connection = self.button_connections[btn]
            btn.clicked.disconnect(old_connection)

        new_connection = lambda checked, c=color: self.attach_color(c)
        btn.clicked.connect(new_connection)

        self.button_connections[btn] = new_connection
        self.color_index = (self.color_index + 1) % len(self.buttons)


    def attach_color(self, color: str):
        clipboard = QApplication.clipboard()
        clipboard.setText(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
