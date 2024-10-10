import pytest
from match import Match
from player import HumanPlayer, Player

# xavier = None
# otto = None

# def setup():
#    global xavier
#    xavier = Player('Xavier')
#    global otto
#    otto = Player('Otto')


# def teardown():
#    global xavier
#    xavier = None
#    global otto
#    otto = None


def test_different_players_have_different_tokens():
    xavier = HumanPlayer('Xavier')
    otto = Player('Otto')
    t = Match(xavier, otto)
    assert xavier.token != otto.token


def test_no_player_with_none_char():
    xavier = HumanPlayer('Xavier')
    otto = Player('Otto')
    t = Match(xavier, otto)
    assert xavier.token != None
    assert otto.token != None


def test_next_player_is_round_robbin():
    xavier = HumanPlayer('Xavier')
    otto = Player('Otto')
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2


def test_players_are_opponents():
    xavier = HumanPlayer('Xavier')
    otto = Player('Otto')
    t = Match(xavier, otto)
    p1 = t.next_player
    p2 = t.next_player
    assert p1.opponent == p2
    assert p2.opponent == p1
