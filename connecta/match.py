class Match:
    def __init__(self, player1, player2):
        player1.token = 'x'
        player2.token = 'o'
        player1.opponent = player2

        self._players = {'x': player1, 'o': player2}
        self._round_robbin = [player1, player2]

    @property
    def next_player(self):
        next = self._round_robbin[0]
        self._round_robbin.reverse()
        return next

    def get_player(self, token):
        return self._players[token]

    def get_winner(self, board):
        """
        Return the winner but in case there is not winner then return None
        """
        for token in self._players.keys():
            if board.is_victory(token):
                return self.get_player(token)
        return None
