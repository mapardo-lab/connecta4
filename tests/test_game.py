import pytest
from game import Game
from squared_board import SquaredBoard


def test_creation():
    g = Game()
    assert g is not None


def test_is_game_over():
    g = Game()

    unfinished = SquaredBoard.fromList(
        [
            ['x', 'o', 'x', None],
            ['x', 'o', 'x', 'x'],
            ['o', 'x', 'o', 'o'],
            ['o', 'x', 'o', 'x'],
        ]
    )
    tie = SquaredBoard.fromList(
        [
            ['x', 'o', 'x', 'o'],
            ['o', 'o', 'x', 'x'],
            ['x', 'x', 'o', 'o'],
            ['o', 'x', 'o', 'x'],
        ]
    )
    win_o = SquaredBoard.fromList(
        [
            ['x', 'o', None, None],
            ['o', 'o', 'o', None],
            ['x', None, None, None],
            ['o', 'x', 'o', 'x'],
        ]
    )
    win_x = SquaredBoard.fromList(
        [
            ['o', 'o', None, None],
            ['x', 'o', 'x', None],
            ['x', 'x', None, None],
            ['o', 'x', 'x', None],
        ]
    )
    assert g._is_game_over() is False

    g.board = unfinished
    assert g._is_game_over() is False

    g.board = tie
    assert g._is_game_over() is True

    g.board = win_x
    assert g._is_game_over() is True

    g.board = win_o
    assert g._is_game_over() is True
