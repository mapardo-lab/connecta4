from oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from squared_board import SquaredBoard
import random


class Player:
    def __init__(self, name, token=None, oracle=BaseOracle(), opponent=None):
        self.name = name
        self.token = token
        self._oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self

    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oráculo
        """
        (best, recommendations) = self._ask_oracle(board)
        self._play_on(board, best.index)

    def _ask_oracle(self, board):
        recommendations = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendations)
        return (best, recommendations)

    def _play_on(self, board, position):
        board.add(self.token, position)
        self.last_move = position

    def _choose(self, recommendations):
        """
        Selecciona la mejor opción entre las recomendaciones
        """
        select = list(
            filter(lambda x: x.classification == ColumnClassification.MAYBE, recommendations)
        )
        return random.choice(select)


class HumanPlayer(Player):
    def __init__(self, name, token=None):
        super().__init__(name, token)

    def _ask_oracle(self, board):
        """
        Le pido al humano que es mi oraculo
        """
        while True:
            # pedimos columna
            raw = input('Select a column: ')
            # comprobamos que es correcto lo introducido
            if _is_valid(board, raw):
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)


def _is_valid(board, raw):
    return (
        _is_int(raw)
        and _is_within_column_range(board, int(raw))
        and _is_non_full_column(board, int(raw))
    )


def _is_int(aString):
    try:
        int(aString)
        return True
    except ValueError:
        return False


def _is_within_column_range(board, num):
    return num >= 0 and num < len(board)


def _is_non_full_column(board, num):
    return not board._columns[num].is_full()
