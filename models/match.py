from models.player import PlayerModel


class MatchModel:
    def __init__(self, pair):
        self.p1 = pair[0][0]
        self.p2 = pair[1][0]
        self.s1 = pair[0][1]
        self.s2 = pair[1][1]

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
