from connecta.linear_board import LinearBoard
from connecta.settings import BOARD_LENGTH, VICTORY_STRIKE


class SquaredBoard:
    """
    Clase que representa un tablero cuadrado de BOARD_LENGTH x BOARD_LENGTH
    None casilla vacia
    """

    def __init__(self):
        """
        Una lista de instancia LinearBoard
        """
        self.board = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def is_full(self):
        """
        Comprueba si esta completo el tablero
        """
        return all(column.is_full() for column in self.board)

    # TODO
    def add(self, token, column):
        """
        Juega en la columna column la ficha token
        """
        self.board[column].add()
