from models.round import RoundModel
from random import choice

class RoundController:
    def __init__(self, round_view):
        self.view = round_view
        self.previous_rounds = []

    def create_round(self, current_round):
        round_name = f"Round {current_round}"
        round = RoundModel(round_name)
        return round
    
    def pair_players(self, players):
        pairs = []
        while len(players) >= 2:
            p1 = players.pop(0)
            p2 = self.find_p2(p1, players)
            pairs.append((p1, p2))
        return pairs
    
    def find_p2(self, p1, players):
        if len(players) > 1:
            if players[0].points == players[1].points:
                candidates = self.find_candidates(p1, players)
                if len(candidates) > 0:
                    chosen = choice(candidates)
                    chosen_index = players.index(chosen)
                    return players.pop(chosen_index)
        return players.pop(0)

    def find_candidates(self, p1, players):
        reference = players[0].points
        candidates = []
        for player in players:
            if player.points != reference:
                break
            elif self.check_already_met(p1, player):
                continue
            else:
                candidates.append(player)
        return candidates
    
    def check_already_met(self, p1, candidate):
        for round in self.previous_rounds:
            for match in round.matchs:
                if (match.p1, match.p2) in [(p1, candidate), (candidate, p1)]:
                    return True
        return False
    
    def run_round(self, pairs, round, match_controller):
        matchs = []
        self.view.display_round_number(round)
        for pair in pairs:
            match = match_controller.create_match(pair)
            match_controller.run_match(match)
            matchs.append(match)
        return matchs
