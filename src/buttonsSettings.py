from mainWindow import *

class Buttons(Ui_MainWindow):
    def initButtons(self):
        self.pushButton_pvp.clicked.connect(lambda: self.runGame('pvp'))
        self.pushButton_pvc.clicked.connect(lambda: self.runGame('pvc'))
        self.pushButton_cvc.clicked.connect(lambda: self.runGame('cvc'))

        self.button_pos00.clicked.connect(lambda: self.setSymbol(self.button_pos00))
        self.button_pos01.clicked.connect(lambda: self.setSymbol(self.button_pos01))
        self.button_pos02.clicked.connect(lambda: self.setSymbol(self.button_pos02))
        self.button_pos10.clicked.connect(lambda: self.setSymbol(self.button_pos10))
        self.button_pos11.clicked.connect(lambda: self.setSymbol(self.button_pos11))
        self.button_pos12.clicked.connect(lambda: self.setSymbol(self.button_pos12))
        self.button_pos20.clicked.connect(lambda: self.setSymbol(self.button_pos20))
        self.button_pos21.clicked.connect(lambda: self.setSymbol(self.button_pos21))
        self.button_pos22.clicked.connect(lambda: self.setSymbol(self.button_pos22))

    def gameModeOn(self):
        self.button_pos00.setEnabled(True)
        self.button_pos01.setEnabled(True)
        self.button_pos02.setEnabled(True)
        self.button_pos10.setEnabled(True)
        self.button_pos11.setEnabled(True)
        self.button_pos12.setEnabled(True)
        self.button_pos20.setEnabled(True)
        self.button_pos21.setEnabled(True)
        self.button_pos22.setEnabled(True)

        self.pushButton_pvp.setVisible(False)
        self.pushButton_pvc.setVisible(False)
        self.pushButton_cvc.setVisible(False)

    def gameModeOff(self):
        self.button_pos00.setDisabled(True)
        self.button_pos01.setDisabled(True)
        self.button_pos02.setDisabled(True)
        self.button_pos10.setDisabled(True)
        self.button_pos11.setDisabled(True)
        self.button_pos12.setDisabled(True)
        self.button_pos20.setDisabled(True)
        self.button_pos21.setDisabled(True)
        self.button_pos22.setDisabled(True)