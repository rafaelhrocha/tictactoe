from mainWindow import Ui_MainWindow 

class Configuration(Ui_MainWindow):
    def __init__(self) -> None:
        self.rounds = 0

    def gameSelectPvP(self):
        
        if self.rounds == 0:
            self.enablePosition(True)
            print("PvP")


    
    def gameSelectCvC(self):
        print("CvC")

    def gameSelectPvC(self):
        print("PvC")


    def checkIfGameEnd(self):
        if self.button_pos00.text() == self.button_pos01.text() and \
        self.button_pos01.text() == self.button_pos02.text() and \
        self.button_pos00 != " ":
            return True

        else:
            return False


    