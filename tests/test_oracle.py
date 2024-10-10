from oracle import *
from squared_board import SquaredBoard


def test_base_oracle():
    board = SquaredBoard.fromList(
        [
            [None, None, None, None],
            ['x', 'o', 'o', 'x'],
            ['x', 'o', 'o', 'x'],
            [None, None, None, None],
        ]
    )
    expected = [
        ColumnRecommendation(0, ColumnClassification.MAYBE),
        ColumnRecommendation(1, ColumnClassification.FULL),
        ColumnRecommendation(2, ColumnClassification.FULL),
        ColumnRecommendation(3, ColumnClassification.MAYBE),
    ]

    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected


def test_equality():
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr == cr
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr != ColumnRecommendation(1, ColumnClassification.MAYBE)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)


def test_hash_eq():
    cr1 = ColumnRecommendation(2, ColumnClassification.MAYBE)
    cr2 = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr1.__hash__() == cr2.__hash__()
