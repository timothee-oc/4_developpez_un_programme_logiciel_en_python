from models.match import MatchModel

class RoundModel:
    def __init__(self, name, matchs=[]):
        self.name = name
        self.matchs = matchs

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "name": self.name,
            "matchs": [match.serialize() for match in self.matchs]
        }
    
    @classmethod
    def deserialize(cls, data: dict) -> 'RoundModel':
        return cls(
            name=data["name"],
            matchs=[MatchModel.deserialize(pair) for pair in data["matchs"]]
        )