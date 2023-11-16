from utils import PLAYERS_DIR, save_json


class PlayerModel:
    def __init__(self, first_name, last_name, birth_date, id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = id
        self.points = 0
        self.file_path = f"{PLAYERS_DIR}{self.id}.json"

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "id": self.id
        }
    
    def save(self):
        save_json(self.serialize(), self.file_path)

    @classmethod
    def deserialize(cls, data: dict) -> 'PlayerModel':
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            id=data["id"]
        )
