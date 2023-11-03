from models.player import PlayerModel
from models.round import RoundModel
from utils import TOURNAMENTS_DIR

class TournamentModel:
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

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Lieu: {self.place}\n"
            f"Du {self.start_date} au {self.end_date}\n"
        )
    
    def serialize(self):
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
    
    @classmethod
    def deserialize(cls, data: dict) -> 'TournamentModel':
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
