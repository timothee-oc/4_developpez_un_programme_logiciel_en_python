from utils import PLAYERS_DIR, save_json


class PlayerModel:
    """
    Class that defines what is a player.
    A player has personnal data, a unique id used to name its file in database,
    a number of points set by default at 0 and a path to its file in database.
    """
    def __init__(self, first_name, last_name, birth_date, id_):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id_ = id_
        self.points = 0
        self.file_path = f"{PLAYERS_DIR}{self.id_}.json"

    def __eq__(self, other: object) -> bool:
        """
        To compare two players, compare their unique ID.

        :return bool
        """
        if not isinstance(other, PlayerModel):
            return NotImplemented
        return self.id_ == other.id_

    def serialize(self):
        """
        Used to save player's data as a json format.
        Used when creating player or when saving a tournament's data.
        Points and file path attributes are not saved.

        :return dict()
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "id_": self.id_
        }

    def save(self):
        """
        Used to save a newly created player in its personnal file in database.
        """
        save_json(self.serialize(), self.file_path)

    @classmethod
    def deserialize(cls, data: dict) -> 'PlayerModel':
        """
        Class method used to create Player objects from a json file.
        :params data(dict)
        :return PlayerModel(data)
        """
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            id_=data["id_"]
        )
