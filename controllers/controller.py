from random import shuffle, choice
from json import dump
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player


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

class Controller:
    def __init__(self, view):
        self.view = view
    
    def run(self):
        running = True
        while running:
            self.view.display_main_menu()
            choice = self.view.select_main_menu()
            if choice == '1':
                tournament = Tournament("TOURNAMENT_NAME", "TOURNAMENT_PLACE")
                for player_data in PLAYERS_DATABASE:
                    player = Player(**player_data)
                    tournament.register_player(player)
                self.run_tournament(tournament)
            elif choice == '2':
                player_data = self.view.input_player_data()
                self.save_data(player_data, "players", player_data['player_id'])
            elif choice.upper() == 'X':
                running = False
            else:
                self.view.alert_unknown_choice()

    def run_tournament(self, tournament):
        shuffle(tournament.players)
        while tournament.current_round <= tournament.number_of_rounds:
            round_name = f"Round {str(tournament.current_round)}"
            round = Round(round_name)
            self.run_round(round, tournament.players)
            tournament.store_round(round)
            tournament.next_round()
            tournament.players = self.sort_by_points(tournament.players)
            self.view.display_ranking(tournament.players)

    def run_round(self, round, players):
        pairs = self.generate_pairs(players.copy())
        for pair in pairs:
            match = Match(pair)
            self.run_match(match)
            round.store_match(match)

    def generate_pairs(self, players):
        pairs = []
        while len(players) >= 2:
            p1 = players.pop(0)
            p2 = self.find_pair(p1, players)
            pairs.append((p1, p2))
            players = self.sort_by_points(players)
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
    
    def sort_by_points(self, players):
        return sorted(players, key=lambda p: p.points, reverse=True)
    
    def run_match(self, match):
        winner = self.random_winner(match)
        match.set_scores(winner)
        self.update_players_points(match)
        self.players_have_met(match)
        
    def random_winner(self, match):
        return choice([match.player1, match.player2, None])
    
    def update_players_points(self, match):
        match.player1.add_points(match.score1)
        match.player2.add_points(match.score2)

    def players_have_met(self, match):
        match.player1.add_met(match.player2)
        match.player2.add_met(match.player1)

    def save_data(self, data, data_dir, file_name):
        file_path = f"data/{data_dir}/{file_name}.json"
        with open(file_path, 'w', encoding='utf-8') as fp:
            dump(data, fp, ensure_ascii=False, indent=4)