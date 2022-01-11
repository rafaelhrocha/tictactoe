from checkButtons import *
from PyQt5 import QtWidgets
import sys



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    game = Buttons()
    game.setupUi(MainWindow)
    game.checkPressedButons()

    MainWindow.show()
    sys.exit(app.exec_())






