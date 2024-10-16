from copy import deepcopy
from enum import Enum, auto

from linear_board import LinearBoard
from settings import BOARD_LENGTH
from squared_board import SquaredBoard


class ColumnClassification(Enum):
    FULL = -1
    LOSE = 1
    MAYBE = 10
    WIN = 100


class ColumnRecommendation:
    def __init__(self, i, c):
        self.index = i
        self.classification = c

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.classification == other.classification

    def __hash__(self):
        return hash(self.classification)


class BaseOracle:

    def _get_column_recommendation(self, board, index, player):
        """
        Classifies a column as either FULL or MAYBE and returns an ColumnRecommendation
        """
        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL
        return ColumnRecommendation(index, classification)

    def get_recommendation(self, board, player):
        """
        Returns a list of ColumnRecommendations
        """
        recommendations = []
        for index in range(len(board)):
            recommendations.append(self._get_column_recommendation(board, index, player))
        return recommendations


class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board, index, player):
        """
        Afina la clasificacion de super e intenta encontrar columnas WIN
        """
        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.LOSE
        return recommendation

    def _is_losing_move(self, board, index, player):
        """
        Determina si al jugar en una posición das la victoria inmediata al contrincante
        """
        # Jugar en la posicion a revisar
        tmp = self._play_on_tmp_board(board, index, player)
        # Chequear si el oponente gana en alguna posición
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp, i, player.opponent):
                return True
        return False

    def _is_winning_move(self, board, index, player):
        """
        Determina si al jugar en una posición hay victoria inmediata
        """
        tmp = self._play_on_tmp_board(board, index, player)
        return tmp.is_victory(player.token)

    def _play_on_tmp_board(self, board, index, player):
        """
        Crea copia del board y juega
        """
        tmp = deepcopy(board)
        tmp.add(player.token, index)
        return tmp
