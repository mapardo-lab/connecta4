import pytest

from connecta.settings import BOARD_LENGTH, VICTORY_STRIKE
from connecta.squared_board import *


def test_empty_board():
    empty = SquaredBoard()
    assert empty is not None
    assert empty.is_full() is False
    assert empty.is_victory("x") is False
    assert empty.is_victory("o") is False


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
