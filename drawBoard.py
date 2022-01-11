from mainWindow import Ui_MainWindow

class Board(Ui_MainWindow):
    def enablePosition(self, enable):
        self.button_pos00.setVisible(enable)
        self.button_pos01.setVisible(enable)
        self.button_pos02.setVisible(enable)
        self.button_pos10.setVisible(enable)
        self.button_pos11.setVisible(enable)
        self.button_pos12.setVisible(enable)
        self.button_pos20.setVisible(enable)
        self.button_pos21.setVisible(enable)
        self.button_pos22.setVisible(enable)

    def updateSymbol(self, symbol, pressed_button):
        if(self.checkButtonIsEnable(pressed_button)):
            pressed_button.setText(symbol)
        

