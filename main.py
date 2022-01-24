from game import Game
from PyQt5 import QtWidgets
import sys



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    game = Game()
    game.setupUi(MainWindow)
    game.start()


    MainWindow.show()
    sys.exit(app.exec_())






