import random

from beautifultable import BeautifulTable
from list_utils import all_same
from oracle import BaseOracle, ColumnClassification, ColumnRecommendation
from settings import BOARD_LENGTH
from squared_board import SquaredBoard


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
        recommendations = sorted(
            recommendations, key=lambda x: x.classification.value, reverse=True
        )
        if all_same(recommendations):
            return random.choice(recommendations)
        else:
            return recommendations[0]


class HumanPlayer(Player):
    def __init__(self, name, token=None, oracle=BaseOracle()):
        super().__init__(name, token, oracle)

    def _ask_oracle(self, board):
        """
        Le pido al humano que es mi oraculo
        """
        while True:
            # pedimos columna
            raw = input('Select a column (type h for help): ')
            # comprobamos que es correcto lo introducido
            if raw == 'h':
                self.display_help(board)
            elif _is_valid(board, raw):
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)

    def display_help(self, board):
        """
        Imprime la tabla con la ayuda solicitada por el jugador humano
        """
        recommendations = self._oracle.get_recommendation(board, self)
        matrix = list(map(lambda x: x.classification.name, recommendations))
        # crear la tabla
        bt = BeautifulTable()
        bt.rows.insert(1, matrix)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        # imprimirla
        print(bt)


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
