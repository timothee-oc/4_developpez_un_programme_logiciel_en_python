from models.match import MatchModel
from random import choice

class MatchController:
    def __init__(self, match_view):
        self.view = match_view

    def create_match(self, pair):
        match = MatchModel(([pair[0], 0], [pair[1], 0]))
        return match

    def run_match(self, match):
        # winner = self.view.input_winner(match)
        winner = self.random_winner() # JUSTE POUR TESTER
        self.set_scores(winner, match)
        match.p1.points += match.s1
        match.p2.points += match.s2

    def set_scores(self, winner, match):
        if winner == '1':
            match.s1 = 1
        elif winner == '2':
            match.s2 = 1
        else:
            match.s1 = match.s2 = 0.5

    def random_winner(self):
        possible_outcomes = ['0', '1', '2']
        winner = choice(possible_outcomes)
        return winner