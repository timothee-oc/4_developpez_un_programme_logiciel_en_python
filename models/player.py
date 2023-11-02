class PlayerModel:
    def __init__(self, first_name, last_name, birth_date, id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = id
        self.points = 0

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}\n"
            f"Né(e) le {self.birth_date}\n"
            f"INE: {self.id}\n"
        )
    
    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "id": self.id
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'PlayerModel':
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            id=data["id"]
        )