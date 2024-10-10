from list_utils import find_strike
from settings import BOARD_LENGTH, VICTORY_STRIKE


class LinearBoard:
    """
    Clase que representa un tablero de una sola columna
    None casilla vacia
    """

    @classmethod
    def fromList(cls, list_tokens):
        board = cls()
        if len(list_tokens) > BOARD_LENGTH:
            raise Exception('Lista de elementos demasiado larga')
        else:
            for i in range(len(list_tokens), BOARD_LENGTH):
                list_tokens.append(None)
            board._column = list_tokens
            return board

    def __init__(self):
        """
        Una lista de None
        """
        self._column = [None for _ in range(BOARD_LENGTH)]

    def is_full(self):
        """
        Comprueba si está completo el tablero
        """
        return self._column[-1] is not None

    def is_victory(self, token):
        """
        Comprueba si hay victoria del jugador token
        """
        return find_strike(self._column, token, VICTORY_STRIKE)

    #        line_string = ''.join(list(filter(lambda x: x is not None, self._column)))
    #        return token * 3 in line_string

    def add(self, token):
        """
        Juega en la primera posición disponible si es que hay
        """
        if not self.is_full():
            self._column[self._column.index(None)] = token

    def is_tie(self, token1, token2):
        """
        Comprueba si no hay victoria de token1 ni token2
        """
        return not self.is_victory(token1) and not self.is_victory(token2)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._column == other._column

    def __hash__(self):
        return hash(self._column)
