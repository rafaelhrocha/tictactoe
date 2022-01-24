from checkButtons import Buttons
from drawBoard import Board
from gameConfiguration import Configuration

class Game(Buttons, Board, Configuration):
    def __init__(self) -> None:
        super().__init__()
        
    def start(self):
        self.checkPressedButons()
        self.enablePosition(False)

