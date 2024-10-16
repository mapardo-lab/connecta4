from enum import Enum, auto

from beautifultable import BeautifulTable
from list_utils import reverse_list_of_lists
from match import Match
from oracle import BaseOracle, SmartOracle
from player import HumanPlayer, Player
from settings import BOARD_LENGTH
from squared_board import SquaredBoard


class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Game:

    def __init__(
        self, round_type=RoundType.COMPUTER_VS_COMPUTER, match=Match(Player('Chip'), Player('Chop'))
    ):
        self.round_type = round_type
        self.match = match
        self.board = SquaredBoard()

    def start(self):
        # imprimo el nombre o logo del juego
        # self.print_logo()
        # configuro partida
        self._configure_by_user()
        # arranco el game loop
        self._start_game_loop()

    def _start_game_loop(self):
        # bucle infinito
        while True:
            # obtengo jugador de turno
            current_player = self.match.next_player
            # le hago jugar
            current_player.play(self.board)
            # muestro su jugada
            self.display_move(current_player)
            # imprimo tablero
            self.display_board()
            # si el juego ha terminado ...
            if self._is_game_over():
                # muestro resultado final
                self.display_result()
                # salgo del bucle
                break

    def display_move(self, player):
        print(f'\n{player.name} ({player.token}) has moved in column {player.last_move}')

    def display_board(self):
        """
        Imprimir tablero en estado actual
        """
        # obtener una matriz de caracteres a partir del tablero
        matrix = self.board.as_list()
        matrix = reverse_list_of_lists(matrix)
        # crear la tabla
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        # imprimirla
        print(bt)

    def display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f'\n{winner.name} ({winner.token}) wins!!!')
        else:
            print(
                f'\nA tie between {self.match.get_player("x").name} (x) and {self.match.get_player("o").name} (o)'
            )

    def _is_game_over(self):
        """
        Game is over when there is a winner or it is a tie
        """
        winner = self.match.get_winner(self.board)
        if winner is not None:
            return True
        elif self.board.is_full():
            return True
        return False

    def _configure_by_user(self):
        """
        Le pido al usuario valores de configuración del tipo de partida y nivel de dificultad
        """
        # tipo de partida
        self.round_type = self._get_round_type()
        # preguntar nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()
        # crear partida
        self.match = self._make_match()

    def _get_difficulty_level(self):
        """
        Pregunta al usuario como de listo quiere que sea su oponente
        """
        print(
            """
        Choose your opponent:
        1) Bender
        2) T-800
        3) T-1000
        """
        )
        while True:
            respond = input("Please type 1, 2 or 3: ").strip()
            if respond == '1':
                return DifficultyLevel.LOW
            elif respond == '2':
                return DifficultyLevel.MEDIUM
            elif respond == '3':
                return DifficultyLevel.HIGH

    def _get_round_type(self):
        """
        Preguntamos al usuario tipo de partida
        """
        print(
            """
        Select type of round:

        1) Computer vs Computer
        2) Computer vs Human
        """
        )
        response = ""
        while response != "1" and response != "2":
            response = input('Please type either 1 or 2: ')
        if response == '1':
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def _make_match(self):

        _levels = {
            DifficultyLevel.LOW: BaseOracle(),
            DifficultyLevel.MEDIUM: SmartOracle(),
            DifficultyLevel.HIGH: SmartOracle(),
        }
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = Player('T-X', oracle=SmartOracle())
            player2 = Player('T-1000', oracle=SmartOracle())
        else:
            player1 = Player('T-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=input('Enter your name: '), oracle=SmartOracle())
        return Match(player1, player2)


#    def print_logo(self):
#        logo = pyfiglet.Figlet(font='stop')
#        print(logo.renderText('Connecta'))
