from mainWindow import Ui_MainWindow
from collections import namedtuple
import config

class Game(Ui_MainWindow):
    def start(self):
        self.reset()
        self.initButtons()

    def reset(self):
        self.turns = 1
        self.playerOne =  namedtuple("pOne", config.playerOne.keys())(*config.playerOne.values())
        self.playerTwo =  namedtuple("pOne", config.playerTwo.keys())(*config.playerTwo.values())

    def initButtons(self):
        self.pushButton_pvp.clicked.connect(lambda: self.runGame('pvp'))

    def runGame(self, gameMode):
        
