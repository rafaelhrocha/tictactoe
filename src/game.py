from email import message
import config
import numpy as np
from collections import namedtuple
from buttonsSettings import Buttons

class Game(Buttons):
    def start(self):
        self.matrix = np.matrix("'' '' '';'' '' '';'' '' ''")
        self.setConfig()
        self.initButtons()
        self.gameModeOff()

    def resetTurns(self):
        self.turns = 1

    def setTurns(self):
        self.turns += 1

    def getTurns(self):
        return self.turns

    def setConfig(self):
        self.playerOne =  namedtuple("pOne", config.playerOne.keys())(*config.playerOne.values())
        self.playerTwo =  namedtuple("pTwo", config.playerTwo.keys())(*config.playerTwo.values())

    def isLocalAvailable(self, local):
        if local.text() == '':
            return True
        else:
            return False

    def winCondition(self, local):
        # if self.getTurns() == 9:
            self.setPlayerText(message.message)

    def setSymbolOnMatrix(self, local, symbol):
        i = int(local.objectName()[10])
        j = int(local.objectName()[11])
        self.matrix[i, j] = symbol
        print(self.matrix)


    def setSymbol(self, local): # fazer um dica como : 1 = p1 , 2 = p2 para melhorar essa parte
        isAvailable = self.isLocalAvailable(local)
        if isAvailable:
            turn = self.getTurns()
            if turn in self.playerOne.turns:
                local.setText(self.playerOne.symbol)
                self.setSymbolOnMatrix(local, self.playerOne.symbol)
                self.setTurns()
                self.setPlayerText(self.playerTwo)
                
            elif turn in self.playerTwo.turns:
                local.setText(self.playerTwo.symbol)  
                self.setSymbolOnMatrix(local, self.playerTwo.symbol)
                self.setTurns()
                self.setPlayerText(self.playerOne)

            self.winCondition(None)
            
    def setPlayerText(self, message):
        self.header_text.setText(message.message)
    
    def runGame(self, gameMode):
        if( gameMode == 'pvp'):
            self.resetTurns()
            self.gameModeOn()
            self.setPlayerText(self.playerOne)
            