import pytest
from linear_board import *
from settings import BOARD_LENGTH, VICTORY_STRIKE


def test_empty_board():
    empty = LinearBoard()
    assert empty is not None
    assert empty.is_full() is False
    assert empty.is_victory("x") is False
    assert empty.is_victory("o") is False


def test_add_to_full_board():
    b = LinearBoard()
    for i in range(BOARD_LENGTH + 1):
        b.add("x")
    assert b.is_full() is True


def test_add():
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add("x")
    assert b.is_full() is True


def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x")
    assert b.is_victory("x") is True
    assert b.is_victory("o") is False


def test_tie():
    b = LinearBoard()
    b.add("x")
    b.add("o")
    b.add("x")
    b.add("o")
    assert b.is_tie("x", "o") is True


def test_equality():
    b = LinearBoard()
    b.add("x")
    c = LinearBoard()
    c.add("o")
    a = LinearBoard()
    a.add("x")
    assert b == a
    assert b != c
