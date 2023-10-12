from round import Round
from random import shuffle


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

    def run(self):
        shuffle(self.players)
        for i in range(self.number_of_rounds):
            round_name = f"Round {str(self.current_round)}"
            round = Round(round_name, self.players.copy())
            round.run()
            self.rounds.append(round)
            self.current_round += 1
            self.players = sorted(self.players,
                                  key=lambda p: p.points,
                                  reverse=True)
            self.print_ranking()

    def print_ranking(self):
        for player in self.players:
            print(player, player.points)
        print()
