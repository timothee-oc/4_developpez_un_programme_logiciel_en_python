from models import TournamentModel, RoundModel, MatchModel
from utils import TOURNAMENTS_DIR, extract_json, list_data_files
from random import shuffle, choice
from datetime import datetime


class TournamentController:
    def __init__(self, tournament_view):
        self.view = tournament_view
        self.tournament = None

    def create_tournament(self):
        tournament_data = self.view.input_tournament_data()
        self.tournament = TournamentModel(**tournament_data)
        self.tournament.save()
        self.view.inform_created()

    def search_tournament(self):
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        while True:
            name = self.view.input_tournament_name()
            if f"{name}.json" in tournaments_files:
                file_path = f"{TOURNAMENTS_DIR}{name}.json"
                tournament_data = extract_json(file_path)
                self.tournament = TournamentModel.deserialize(tournament_data)
                break
            elif name == '':
                self.tournament = None
                break
            else:
                self.view.alert_not_existing(name)

    def register_players(self, player_controller):
        self.search_tournament()
        if self.tournament:
            player_controller.list_all_players()
            while True:
                self.view.display_registered_players(self.tournament.players)
                player_controller.search_player()
                if player_controller.player:
                   self.tournament.players.append(player_controller.player)
                else:
                    break
            self.tournament.save()

    def check_runnable(self):
        if len(self.tournament.players) == 0:
            self.view.alert_no_players()
            return False
        if len(self.tournament.players) % 2 != 0:
            self.view.alert_not_even()
            return False
        if self.tournament.current_round > self.tournament.number_rounds:
            self.view.alert_already_finished()
            return False
        return True
    
    def set_players_points(self):
        for round in self.tournament.rounds:
            for match in round.matchs:
                match.p1.points += match.s1
                match.p2.points += match.s2

    def check_already_met(self, p1, candidate):
        for round in self.tournament.rounds:
            for match in round.matchs:
                if (match.p1, match.p2) in [(p1, candidate), (candidate, p1)]:
                    return True
        return False

    def find_candidates(self, p1):
        reference = self.tournament.players[0].points
        candidates = []
        for player in self.tournament.players:
            if player.points != reference:
                break
            elif not self.check_already_met(p1, player):
                candidates.append(player)
        return candidates

    def find_p2(self, p1):
        if len(self.tournament.players) > 1 and self.tournament.players[0].points == self.tournament.players[1].points:
            candidates = self.find_candidates(p1)
            if len(candidates) > 0:
                chosen = choice(candidates)
                chosen_index = self.tournament.players.index(chosen)
                return self.tournament.players.pop(chosen_index)
        return self.tournament.players.pop(0)

    def pair_players(self):
        pairs = []
        while len(self.tournament.players) >= 2:
            p1 = self.tournament.players.pop(0)
            p2 = self.find_p2(p1)
            pairs.append((p1, p2))
        return pairs

    def run_match(self, pair):
        match = MatchModel(([pair[0], 0], [pair[1], 0]))
        winner = self.view.input_winner(match)
        if winner == '1':
            match.s1 = 1
        elif winner == '2':
            match.s2 = 1
        else:
            match.s1 = match.s2 = 0.5
        match.p1.points += match.s1
        match.p2.points += match.s2
        return match

    def run_round(self):
        if self.tournament.current_round == 1:
            shuffle(self.tournament.players)
        else:
            self.tournament.players = sorted(self.tournament.players, key=lambda p: p.points, reverse=True)
        pairs = self.pair_players()
        round = RoundModel(name=f"Round {self.tournament.current_round}",start_date_time=datetime.now())
        self.tournament.rounds.append(round)
        self.view.display_round_matchs(round, pairs)
        print(len(pairs))
        for pair in pairs:
            match = self.run_match(pair)
            self.tournament.rounds[-1].matchs.append(match)
            self.tournament.players.extend(pair)
            self.tournament.save()
        round.end_date_time = datetime.now()
        self.tournament.current_round += 1
        self.tournament.save()

    def run_tournament(self):
        self.search_tournament()
        if self.tournament and self.check_runnable():
            self.set_players_points()
            while self.tournament.current_round <= self.tournament.number_rounds:
                self.run_round()

    def list_all_tournaments(self):
        all_tournaments_files = list_data_files(TOURNAMENTS_DIR)
        all_tournaments_data = [
            extract_json(f"{TOURNAMENTS_DIR}{tournament_file}") for tournament_file in all_tournaments_files
        ]
        all_tournaments = [TournamentModel.deserialize(tournament_data) for tournament_data in all_tournaments_data]
        self.view.display_all_tournaments(all_tournaments)

    def display_one_tournament(self):
        self.search_tournament()
        if self.tournament:
            self.view.display_one_tournament(self.tournament)

    def list_tournament_players(self):
        self.search_tournament()
        if self.tournament:
            self.view.display_tournament_players(self.tournament)

    def list_tournament_rounds(self):
        self.search_tournament()
        if self.tournament:
            self.view.display_tournament_rounds(self.tournament)
