class Tournament:
    def __init__(self, name, place, number_of_rounds=4):
        self.name = name
        self.place = place
        self.start_date = None
        self.end_date = None
        self.number_of_rounds = number_of_rounds
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.description = ""

    def __str__(self):
        output = ""
        for round in self.rounds:
            output += f"{round}\n"
        return output

    def __repr__(self):
        return str(self)

    def register_player(self, player):
        self.players.append(player)

    def store_round(self, round):
        self.rounds.append(round)

    def next_round(self):
        self.current_round += 1

    def sort_by_points(self):
        self.players = sorted(self.players, key=lambda p: p.points, reverse=True)

    def reset_players_pairs(self, pairs):
        for p1, p2 in pairs:
            self.players.append(p1)
            self.players.append(p2)

    def serialize(self):
        return {
            "name": self.name,
            "place": self.place,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "players": [player.serialize() for player in self.players],
            "rounds": [round.serialize() for round in self.rounds]
        }
