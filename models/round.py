from .match import MatchModel
from datetime import datetime


class RoundModel:
    """
    Class defining a round in the tournament.
    A round is a list of matchs object.
    It also has a name and dates of start and finish.
    """
    def __init__(self, name, start_date_time,
                 end_date_time=None, matchs=[]):
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs = matchs

    def serialize(self):
        """
        Used to save round's data in a json file.
        Used when saving a tournament's data.

        :return dict
        """
        return {
            "name": self.name,
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat() if self.end_date_time else None,
            "matchs": [match.serialize() for match in self.matchs]
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'RoundModel':
        """
        Class method used to create Round objects from a json file.
        :params data(dict)
        :return RoundModel(data)
        """
        return cls(
            name=data["name"],
            start_date_time=datetime.fromisoformat(data["start_date_time"]),
            end_date_time=datetime.fromisoformat(data["end_date_time"]) if data["end_date_time"] else None,
            matchs=[MatchModel.deserialize(pair) for pair in data["matchs"]]
        )
