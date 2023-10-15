from random import shuffle, choice
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


PLAYERS_DATABASE = [
    {
        "first_name": "Marie", "last_name": "Martin",
        "date_of_birth": "02-02-2002", "player_id": "CD23456"
    },
    {
        "first_name": "Jean", "last_name": "Bernard",
        "date_of_birth": "03-03-2003", "player_id": "EF34567"
    },
    {
        "first_name": "Jeanne", "last_name": "Thomas",
        "date_of_birth": "04-04-2004", "player_id": "GH45678"
    },
    {
        "first_name": "Pierre", "last_name": "Petit",
        "date_of_birth": "05-05-2005", "player_id": "IJ56789"
    },
    {
        "first_name": "Françoise", "last_name": "Robert",
        "date_of_birth": "05-07-1997", "player_id": "AB12345"
    },
    {
        "first_name": "Michel", "last_name": "Richard",
        "date_of_birth": "01-01-2001", "player_id": "ZY98765"
    },
]

class TournamentController:
    def __init__(self, view):
        self.tournament = None
        self.players_database = []
        self.view = view

    def run(self):
        self.tournament = Tournament("ULTRA_TOURNAMENT", "TOURNAMENT_PLACE")
        self.players_database = [Player(**player_data) for player_data in PLAYERS_DATABASE]
        self.register_players()
        self.run_tournament()
        return self.tournament

    def register_players(self):
        for player in self.players_database:
            self.tournament.register_player(player)

    def run_tournament(self):
        shuffle(self.tournament.players)
        while self.tournament.current_round <= self.tournament.number_of_rounds:
            round_name = f"Round {str(self.tournament.current_round)}"
            round = Round(round_name)
            self.run_round(round)
            self.tournament.store_round(round)
            self.tournament.next_round()
            self.view.display_ranking(self.tournament)

    def run_round(self, round):
        pairs = self.generate_pairs()
        for pair in pairs:
            match = Match(pair)
            self.run_match(match)
            round.store_match(match)
        self.tournament.reset_players_pairs(pairs)
        
    def generate_pairs(self):
        pairs = []
        while len(self.tournament.players) >= 2:
            p1 = self.tournament.players.pop(0)
            p2 = self.find_pair(p1)
            pairs.append((p1, p2))
            self.tournament.sort_by_points()
        return pairs
    
    def find_pair(self, p1):
        p2 = self.tournament.players.pop(0)
        if len(self.tournament.players) != 0:
            if p2 in p1.players_met:
                p2 = self.find_not_met(p1, p2)
                candidates = self.find_candidates(p1, p2)
                if len(candidates) > 1:
                    p2 = self.choose_candidate(candidates)
        return p2
    
    def find_not_met(self, p1, p2):
        players_tested = 0
        while p2 in p1.players_met:
            self.tournament.players.append(p2)
            p2 = self.tournament.players.pop(0)
            players_tested += 1
            if players_tested > len(self.tournament.players):
                break
        return p2
        
    def find_candidates(self, p1, p2):
        candidates = [p2]
        for player in self.tournament.players:
            if player.points != p2.points:
                break
            elif player in p1.players_met:
                continue
            else:
                candidates.append(player)
                self.tournament.players.pop(self.tournament.players.index(player))
        return candidates
    
    def choose_candidate(self, candidates):
        chosen = choice(candidates)
        for candidate in candidates:
            if candidate != chosen:
                self.tournament.players.append(candidate)
        return chosen
    
    def run_match(self, match):
        winner = self.random_winner(match)
        match.set_scores(winner)
        match.player1.add_points(match.score1)
        match.player2.add_points(match.score2)
        match.player1.add_met(match.player2)
        match.player2.add_met(match.player1)
        
    def random_winner(self, match):
        return choice([match.player1, match.player2, None])
