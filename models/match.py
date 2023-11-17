from .player import PlayerModel


class MatchModel:
    """
    Class defining a match in the tournament.
    A match is a pair of players and their respective scores.
    """
    def __init__(self, pair):
        self.player1 = pair[0][0]
        self.player2 = pair[1][0]
        self.score1 = pair[0][1]
        self.score2 = pair[1][1]

    def serialize(self):
        """
        Used to save match's data in a json file.
        Used when saving a tournament's data.

        :return tuple(list[player(PlayerModel), score(int)])
        """
        return (
            [self.player1.serialize(), self.score1],
            [self.player2.serialize(), self.score2]
        )

    @classmethod
    def deserialize(cls, pair) -> 'MatchModel':
        """
        Class method used to create Match objects from a json file.
        :params pair(tuple(list))
        :return MatchModel(tuple(list[PlayerModel(pair[X][0]), pair[X][1]]))
        """
        return cls(
            pair=(
                [PlayerModel.deserialize(pair[0][0]), pair[0][1]],
                [PlayerModel.deserialize(pair[1][0]), pair[1][1]]
            )
        )
