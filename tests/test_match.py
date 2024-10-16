import pytest
from match import Match
from player import HumanPlayer, Player


# Se aplica setup + teardown
@pytest.fixture
def instancias():
    # Este fixture retorna las dos instancias
    xavier = Player('Xavier')
    otto = Player('Otto')
    yield xavier, otto  # 'yield entrega las instancias a las pruebas
    # Despues de las pruebas se limpia (teardown)
    del xavier
    del otto


def test_different_players_have_different_tokens(instancias):
    xavier, otto = instancias
    t = Match(xavier, otto)
    assert xavier.token != otto.token


def test_no_player_with_none_char(instancias):
    xavier, otto = instancias
    #    xavier = HumanPlayer('Xavier')
    #    otto = Player('Otto')
    t = Match(xavier, otto)
    assert xavier.token != None
    assert otto.token != None


def test_next_player_is_round_robbin(instancias):
    xavier, otto = instancias
    #    xavier = HumanPlayer('Xavier')
    #    otto = Player('Otto')
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2


def test_players_are_opponents(instancias):
    xavier, otto = instancias
    #    xavier = HumanPlayer('Xavier')
    #    otto = Player('Otto')
    t = Match(xavier, otto)
    p1 = t.next_player
    p2 = t.next_player
    assert p1.opponent == p2
    assert p2.opponent == p1
