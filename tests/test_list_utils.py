import pytest

from connecta.list_utils import *


def test_find_one():
    needle = 1
    none = [0, "x", "o"]
    beggining = [1, 0, 0, 0]
    end = [6, 5, 4, 3, 2, 1]
    several = [0, 0, 2, 1, 0, 0, 1, 1, 5]
    assert find_one(none, needle) is False
    assert find_one(beggining, needle) is True
    assert find_one(end, needle) is True
    assert find_one(several, needle) is True


def test_find_n():
    assert find_n([2, 3, 4, 5, 6], 2, -1) is False
    assert find_n([1, 2, 3, 4, 5], 42, 2) is False
    assert find_n([1, 2, 3, 4, 5], 1, 2) is False
    assert find_n([1, 2, 3, 4, 2, 5], 2, 2)
    assert find_n([1, 4, 2, 3, 4, 5, 4, 4], 4, 3)
    assert find_n([1, 4, 2, 3, 4, 5, 4, 4], "x", 0) is False
    assert find_n([1, 4, 2, 3, "x"], "x", 0) is False


def test_find_strike():
    assert find_strike([2, 3, 4, 5, 6], 2, -1) is False
    assert find_strike([1, 2, 3, 4, 5], 42, 2) is False
    assert find_strike([1, 2, 3, 4, 5], 4, 1)
    assert find_strike([1, 2, 3, 4, 2, 5], 2, 2) is False
    assert find_strike([1, 4, 2, 3, 4, 5, 5, 5], 5, 3)
    assert find_strike([5, 5, 5, 3, 4, 4, 4], 5, 3)
    assert find_strike([1, 2, 2, 5, 5, 5, 3, 4, 4, 4], 5, 3)
    assert find_strike([1, 2, 2, 5, 5, 5, 4, 4, 4], 5, 4) is False
    assert find_strike([1, 4, 2, 3, "x"], "x", 0) is False
