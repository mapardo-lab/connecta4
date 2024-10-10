import pytest
from settings import BOARD_LENGTH, VICTORY_STRIKE
from squared_board import *


def test_empty_board():
    empty = SquaredBoard()
    assert empty is not None
    assert empty.is_full() is False
    assert empty.is_victory("x") is False
    assert empty.is_victory("o") is False


def test_vertical_victory():
    vertical = SquaredBoard.fromList(
        [
            ['x', 'x', 'x'],
            ['o'],
            ['x'],
            [],
        ]
    )
    assert vertical.is_victory('x')
    assert vertical.is_victory('o') == False


def test_horizontal_victory():
    horizontal = SquaredBoard.fromList(
        [
            ['o', 'x', 'x', None],
            ['o', None, None, None],
            ['o', None, None, None],
            [None, None, None, None],
        ]
    )
    assert horizontal.is_victory('o')
    assert horizontal.is_victory('x') == False


def test_rising_victory():
    rising = SquaredBoard.fromList(
        [
            ['o', 'x', 'x', None],
            ['x', 'o', None, None],
            ['o', 'x', 'o', None],
            [None, None, None, None],
        ]
    )
    assert rising.is_victory('x') == False
    assert rising.is_victory('o')


def test_sinking_victory():
    sinking = SquaredBoard.fromList(
        [
            ['o', 'x', 'x', None],
            ['x', 'o', 'o', None],
            ['x', 'o', None, None],
            ['o', None, None, None],
        ]
    )
    assert sinking.is_victory('x') == False
    assert sinking.is_victory('o')


def test_add():
    b = SquaredBoard()
    for column in range(BOARD_LENGTH):
        for i in range(BOARD_LENGTH):
            b.add("x", column)
    assert b.is_full() is True


def test_add_to_full_board():
    b = SquaredBoard()
    for column in range(BOARD_LENGTH):
        for i in range(BOARD_LENGTH):
            b.add("x", column)
    b.add("x", 0)
    assert b.is_full() is True


def test_victory():
    b = SquaredBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x", 0)
    assert b.is_victory("x") is True
    assert b.is_victory("o") is False


def test_tie():
    b = SquaredBoard()
    b.add("x", 0)
    b.add("o", 0)
    b.add("x", 0)
    b.add("o", 0)
    assert b.is_tie("x", "o") is True


def test_eq():
    board1 = SquaredBoard.fromList(
        [
            [None, None, None, None],
            ['x', 'o', 'x', 'x'],
            ['o', 'o', 'x', 'x'],
            [None, None, None, None],
        ]
    )
    board2 = SquaredBoard.fromList(
        [
            ['x', None, None, None],
            ['x', 'o', 'x', 'x'],
            ['o', 'o', 'x', 'x'],
            [None, None, None, None],
        ]
    )

    assert board1 == board1
    assert board1 != board2

    board1.add('x', 0)

    assert board1 == board2
