from models.round import RoundModel
from models.match import MatchModel
from random import choice, shuffle

class RoundController:
    def __init__(self, view):
        self.view = view

    def create_round(self, tournament):
        round_name = f"Round {tournament.current_round}"
        round = RoundModel(round_name)
        if tournament.current_round == 1:
            shuffle(tournament.players)
        else:
            tournament.sort_by_points()
        return round
    
    def pair_players(self, tournament):
        pairs = []
        while len(tournament.players) >= 2:
            p1 = tournament.players.pop(0)
            p2 = self.find_p2(p1, tournament)
            pair = (p1, p2)
            pairs.append(pair)
        return pairs
    
    def find_p2(self, p1, tournament):
        if len(tournament.players) > 1:
            if tournament.players[0].points == tournament.players[1].points:
                reference = tournament.players[0].points
                candidates = self.find_candidates(p1, tournament.players, reference)
                if len(candidates) > 0:
                    chosen = choice(candidates)
                    chosen_index = tournament.players.index(chosen)
                    return tournament.players.pop(chosen_index)
        return tournament.players.pop(0)

    def find_candidates(self, p1, others, reference, tournament):
        candidates = []
        for player in others:
            if player.points != reference:
                break
            elif self.check_already_met(p1, player, tournament):
                continue
            else:
                candidates.append(player)
        return candidates
    
    def check_already_met(self, p1, candidate, tournament):
        for round in tournament.rounds:
            for match in round.matchs:
                if (match.p1, match.p2) in [(p1, candidate), (candidate, p1)]:
                    return True
        return False
    
    def run_round(self, pairs):
        matchs = []
        for pair in pairs:
            match = MatchModel(([pair[0], 0], [pair[1], 0]))
            # winner = self.view.input_winner(match)
            winner = match.random_winner() # JUSTE POUR TESTER
            match.set_scores(winner)
            match.p1.points += match.s1
            match.p2.points += match.s2
            matchs.append(match)
        return matchs
