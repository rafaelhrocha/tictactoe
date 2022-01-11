from mainWindow import Ui_MainWindow 

class Buttons(Ui_MainWindow):
    def __init__(self) -> None:
        pass

    def checkPressedButons(self):
        self.button_pos00.clicked.connect(lambda: self.updateDrawBoard( self.button_pos00, self.symbol))
        self.button_pos01.clicked.connect(lambda: self.updateDrawBoard( self.button_pos01, self.symbol))
        self.button_pos02.clicked.connect(lambda: self.updateDrawBoard( self.button_pos02, self.symbol))
        self.button_pos10.clicked.connect(lambda: self.updateDrawBoard( self.button_pos10, self.symbol))
        self.button_pos11.clicked.connect(lambda: self.updateDrawBoard( self.button_pos11, self.symbol))
        self.button_pos12.clicked.connect(lambda: self.updateDrawBoard( self.button_pos12, self.symbol))
        self.button_pos20.clicked.connect(lambda: self.updateDrawBoard( self.button_pos20, self.symbol))
        self.button_pos21.clicked.connect(lambda: self.updateDrawBoard( self.button_pos21, self.symbol))
        self.button_pos22.clicked.connect(lambda: self.updateDrawBoard( self.button_pos22, self.symbol))

        self.pushButton_cvc.clicked.connect(lambda: self.gameSelect("CVC"))
        self.pushButton_pvc.clicked.connect(lambda: self.gameSelect("PVC"))
        self.pushButton_pvp.clicked.connect(lambda: self.gameSelect("PVP"))

        






