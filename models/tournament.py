from .player import PlayerModel
from .round import RoundModel
from utils import TOURNAMENTS_DIR, save_json


class TournamentModel:
    """
    Class defining a tournament.
    A tournament has a list of registered players and a list of rounds.
    It also has a name, a place, start and finish dates, a total number of rounds,
    as well as the number of the current round being played, and a path to its file
    in database.
    """
    def __init__(self, name, place, start_date, end_date,
                 number_rounds=4, current_round=1, rounds=[],
                 players=[], description=""):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_rounds = number_rounds
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.description = description
        self.file_path = f"{TOURNAMENTS_DIR}{self.name}.json"

    def serialize(self):
        """
        Used to save tournament's data in a json file.

        :return dict() 
        """
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_rounds": self.number_rounds,
            "current_round": self.current_round,
            "rounds": [round.serialize() for round in self.rounds],
            "players": [player.serialize() for player in self.players],
            "description": self.description
        }

    def save(self):
        """
        Used when creating a new tournament or between matchs and rounds
        during run, to allow for exting and starting again.
        """
        save_json(self.serialize(), self.file_path)

    @classmethod
    def deserialize(cls, data: dict) -> 'TournamentModel':
        """
        Class method used to create Tournament objects from a json file.
        :params data(dict)
        :return TournamentModel(data)
        """
        return TournamentModel(
            name=data["name"],
            place=data["place"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            number_rounds=data["number_rounds"],
            current_round=data["current_round"],
            rounds=[RoundModel.deserialize(round_data) for round_data in data["rounds"]],
            players=[PlayerModel.deserialize(player_data) for player_data in data["players"]],
            description=data["description"]
        )
