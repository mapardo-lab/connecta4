from linear_board import LinearBoard
from list_utils import move_down_list_of_lists, reverse_list_of_lists, transpose
from settings import BOARD_LENGTH, VICTORY_STRIKE


class SquaredBoard:
    """
    Clase que representa un tablero cuadrado de BOARD_LENGTH x BOARD_LENGTH
    None casilla vacia
    """

    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma un lista de listas en una lista de LinearBoard
        """
        board = cls()
        if len(list_of_lists) > BOARD_LENGTH:
            raise Exception("Demasiadas columnas")
        else:
            board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
            return board

    def __init__(self):
        """
        Una lista de instancias LinearBoard
        """
        self._columns = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def is_full(self):
        """
        Comprueba si esta completo el tablero
        """
        return all(column.is_full() for column in self._columns)

    def as_list(self):
        """
        Convierte el tablero en una lista de listas
        """
        return list(map(lambda x: x._column, self._columns))

    def is_victory(self, token):
        """
        Comprueba si hay victoria del jugador token
        """
        return (
            self._any_vertical_victory(token)
            or self._any_horizontal_victory(token)
            or self._any_rising_victory(token)
            or self._any_sinking_victory(token)
        )

    def _any_vertical_victory(self, token):
        """
        Comprueba si hay victoria en vertical del jugador token
        """
        return any(column.is_victory(token) for column in self._columns)

    def _any_horizontal_victory(self, token):
        """
        Comprueba si hay victoria en horizontal del jugador token
        """
        board_transpose = SquaredBoard.fromList(transpose(self.as_list()))
        return board_transpose._any_vertical_victory(token)

    def _any_rising_victory(self, token):
        """
        Comprueba si hay victoria en diagonal ascendente del jugador token
        """
        board_move = SquaredBoard.fromList(move_down_list_of_lists(self.as_list()))
        return board_move._any_horizontal_victory(token)

    def _any_sinking_victory(self, token):
        """
        Comprueba si hay victoria en diagonal descendente del jugador token
        """
        board_move = SquaredBoard.fromList(
            move_down_list_of_lists(reverse_list_of_lists(self.as_list()))
        )
        return board_move._any_horizontal_victory(token)

    def add(self, token, column):
        """
        Juega en la columna column la ficha token
        """
        self._columns[column].add(token)

    def is_tie(self, token1, token2):
        """
        Comprueba si no hay victoria de token1 ni token2
        """
        victory1 = any(column.is_victory(token1) for column in self._columns)
        victory2 = any(column.is_victory(token2) for column in self._columns)
        return not victory1 and not victory2

    def __repr__(self):
        return f'{self.__class__}: {self._columns}'

    def __len__(self):
        return len(self._columns)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns

    def __hash__(self):
        return hash(self._columns)
