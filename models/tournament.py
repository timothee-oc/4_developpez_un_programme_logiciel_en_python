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
