from random import choice


class Match:
    def __init__(self, players):
        self.players = players
        self.winner_index = None
        self.winner = None
        self.result = ([self.players[0], 0],
                       [self.players[1], 0])

    def __repr__(self) -> str:
        return str(self.result)

    def run(self):
        self.random_winner()
        self.set_scores()
        self.players[0].add_met(self.players[1])
        self.players[1].add_met(self.players[0])

    def set_scores(self):
        if self.winner:
            self.result[self.winner_index][1] = 1
            self.winner.add_points(1)
        else:
            self.result[0][1] = self.result[1][1] = 0.5
            for player in self.players:
                player.add_points(0.5)

    def random_winner(self):
        self.winner = choice([self.players[0], self.players[1], None])
        if self.winner:
            self.winner_index = self.players.index(self.winner)
