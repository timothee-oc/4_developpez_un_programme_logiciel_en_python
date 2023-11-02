from models.player import PlayerModel
from random import choice

class MatchModel:
    def __init__(self, pair):
        self.p1 = pair[0][0]
        self.p2 = pair[1][0]
        self.s1 = pair[0][1]
        self.s2 = pair[1][1]

    def random_winner(self):
        possible_outcomes = ['0', '1', '2']
        winner = choice(possible_outcomes)
        return winner
    
    def set_scores(self, winner):
        if winner == '1':
            self.s1 = 1
        elif winner == '2':
            self.s2 = 1
        else:
            self.s1 = self.s2 = 0.5

    def serialize(self):
        return (
            [self.p1.serialize(), self.s1],
            [self.p2.serialize(), self.s2]
        )
    
    @classmethod
    def deserialize(cls, pair) -> 'MatchModel':
        return cls(
            pair=(
                [PlayerModel.deserialize(pair[0][0]), pair[0][1]],
                [PlayerModel.deserialize(pair[1][0]), pair[1][1]]
            )
        )