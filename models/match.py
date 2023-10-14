class Match:
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.score1 = 0
        self.score2 = 0

    def __str__(self):
        return f"{self.player1} {self.score1} - {self.score2} {self.player2}"

    def __repr__(self):
        return str(self)
    
    def set_scores(self, winner):
        if winner == self.player1:
            self.score1 = 1
        elif winner == self.player2:
            self.score2 = 1
        else:
            self.score1 = self.score2 = 0.5

    def serialize(self):
        return (
            [self.player1.serialize(), self.score1],
            [self.player2.serialize(), self.score2]
        )
