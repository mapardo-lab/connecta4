from enum import Enum, auto

from linear_board import LinearBoard
from settings import BOARD_LENGTH
from squared_board import SquaredBoard


class ColumnClassification(Enum):
    FULL = auto()
    MAYBE = auto()


class ColumnRecommendation:
    def __init__(self, i, c):
        self.index = i
        self.classification = c

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return (self.index, self.classification) == (other.index, other.classification)

    def __hash__(self):
        return hash((self.index, self.classification))


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
