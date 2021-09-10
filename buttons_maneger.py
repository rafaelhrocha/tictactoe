from ttt import Ui_MainWindow
from buttons_functions import *


class Button(Ui_MainWindow, ):
    def __init__(self):
        super().__init__()

    def connections(self):
        self.Button_pos00.clicked.connect()
        