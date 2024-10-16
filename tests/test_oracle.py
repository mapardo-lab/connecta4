from oracle import *
from player import Player
from settings import BOARD_LENGTH
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

    assert cr == ColumnRecommendation(1, ColumnClassification.MAYBE)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)


def test_hash_eq():
    cr1 = ColumnRecommendation(2, ColumnClassification.MAYBE)
    cr2 = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr1.__hash__() == cr2.__hash__()


def test_is_winning_move():
    winner = Player('Xavier', 'x')
    loser = Player('Otto', 'o')

    empty = SquaredBoard()
    almost = SquaredBoard.fromList(
        [
            ['o', 'x', 'o', None],
            ['o', 'x', 'o', None],
            ['x', None, None, None],
            [None, None, None, None],
        ]
    )
    oracle = SmartOracle()

    for i in range(0, BOARD_LENGTH):
        assert oracle._is_winning_move(empty, i, winner) == False
        assert oracle._is_winning_move(empty, i, loser) == False

    for i in range(0, BOARD_LENGTH):
        assert oracle._is_winning_move(almost, i, loser) == False

    assert oracle._is_winning_move(almost, 2, winner)


def test_is_losing_move():
    player_opponent = Player('Otto', 'o')
    player_check = Player('Xavier', 'x', opponent=player_opponent)

    empty = SquaredBoard()
    board1 = SquaredBoard.fromList(
        [
            ['x', None, None, None],
            ['o', None, None, None],
            ['o', None, None, None],
            ['x', None, None, None],
        ]
    )
    board2 = SquaredBoard.fromList(
        [
            ['x', None, None, None],
            ['o', None, None, None],
            ['x', 'o', 'o', None],
            ['x', None, None, None],
        ]
    )
    board3 = SquaredBoard.fromList(
        [
            ['x', None, None, None],
            ['o', None, None, None],
            ['x', 'o', None, None],
            ['x', None, None, None],
        ]
    )
    oracle = SmartOracle()

    for i in range(0, BOARD_LENGTH):
        assert oracle._is_losing_move(empty, i, player_check) == False

    for i in range(0, BOARD_LENGTH):
        assert oracle._is_losing_move(board1, i, player_check) == False

    assert oracle._is_losing_move(board2, 0, player_check)
    assert oracle._is_losing_move(board2, 1, player_check)
    assert oracle._is_losing_move(board2, 2, player_check) == False
    assert oracle._is_losing_move(board2, 3, player_check)

    assert oracle._is_losing_move(board3, 0, player_check) == False
    assert oracle._is_losing_move(board3, 1, player_check) == False
    assert oracle._is_losing_move(board3, 2, player_check) == False
    assert oracle._is_losing_move(board3, 3, player_check)
