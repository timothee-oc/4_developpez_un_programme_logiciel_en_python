from match import Match
from random import choice


class Round:
    def __init__(self, name, players):
        self.matchs = []
        self.name = name
        self.players = players
        self.date_time_start = None
        self.date_time_end = None

    def __repr__(self) -> str:
        return str(self.matchs)

    def run(self):
        pairs = self.generate_pairs(self.players)
        for pair in pairs:
            match = Match(pair)
            match.run()
            self.matchs.append(match)

    def generate_pairs(self, players):
        pairs = []
        while len(players) >= 2:
            p1 = players.pop(0)
            p2 = self.find_pair(p1, players)
            pairs.append((p1, p2))
            players = sorted(players, key=lambda p: p.points, reverse=True)
        return pairs

    def find_pair(self, p1, other_players):
        p2 = other_players.pop(0)
        if len(other_players) != 0:
            players_tested = 0
            while p2 in p1.players_met:
                other_players.append(p2)
                p2 = other_players.pop(0)
                players_tested += 1
                if players_tested > len(other_players):
                    break
            if self.check_same_points_not_met(p1, p2, other_players[0]):
                candidates = self.find_candidates(p1, p2, other_players)
                p2 = self.choose_candidate(p2, candidates, other_players)
        return p2

    def check_same_points_not_met(self, p1, p2, next_one):
        if next_one.points == p2.points and next_one not in p1.players_met:
            return True
        else:
            return False

    def find_candidates(self, p1, p2, other_players):
        candidates = [p2, other_players[0]]
        for player in other_players[1:]:
            if player.points != p2.points:
                break
            elif player in p1.players_met:
                continue
            else:
                candidates.append(player)
        return candidates

    def choose_candidate(self, p2, candidates, other_players):
        chosen = choice(candidates)
        if chosen != p2:
            other_players.append(p2)
            p2 = other_players.pop(other_players.index(chosen))
        return p2
