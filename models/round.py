from .match import MatchModel
from datetime import datetime


class RoundModel:
    def __init__(self, name, start_date_time,
                 end_date_time=None, matchs=[]):
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs = matchs

    def serialize(self):
        return {
            "name": self.name,
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat() if self.end_date_time else None,
            "matchs": [match.serialize() for match in self.matchs]
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'RoundModel':
        return cls(
            name=data["name"],
            start_date_time=datetime.fromisoformat(data["start_date_time"]),
            end_date_time=datetime.fromisoformat(data["end_date_time"]) if data["end_date_time"] else None,
            matchs=[MatchModel.deserialize(pair) for pair in data["matchs"]]
        )
