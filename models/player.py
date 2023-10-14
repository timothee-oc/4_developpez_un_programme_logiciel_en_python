class Player:
    def __init__(self, first_name, last_name, date_of_birth, player_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        self.points = 0
        self.players_met = set()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return str(self)    

    def add_points(self, score):
        self.points += score
        if isinstance(self.points, float) and self.points.is_integer():
            self.points = int(self.points)

    def add_met(self, player):
        self.players_met.add(player)
