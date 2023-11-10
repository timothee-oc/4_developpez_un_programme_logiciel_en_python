from .match import MatchModel
from datetime import datetime


class RoundModel:
    def __init__(self, name, start_date_time,
                 end_date_time=None, matchs=[]):
        self.name = name
        self.matchs = matchs
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time

    def serialize(self):
        return {
            "name": self.name,
            "matchs": [match.serialize() for match in self.matchs],
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat()
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'RoundModel':
        return cls(
            name=data["name"],
            matchs=[MatchModel.deserialize(pair) for pair in data["matchs"]],
            start_date_time=datetime.fromisoformat(data["start_date_time"]),
            end_date_time=datetime.fromisoformat(data["end_date_time"])
        )
