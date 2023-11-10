from models.tournament import TournamentModel
from utils import TOURNAMENTS_DIR, save_json, extract_json, list_data_files
from random import shuffle


class TournamentController:
    def __init__(self, tournament_view):
        self.view = tournament_view
        self.tournament = None

    def save(self):
        save_json(self.tournament.serialize(), self.tournament.file_path)

    def create_tournament(self):
        tournament_data = self.view.input_tournament_data()
        self.tournament = TournamentModel(**tournament_data)
        self.save()
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
                break
            else:
                self.view.alert_not_existing_tournament(name)

    def register_players(self, player_controller):
        player_controller.list_all_players()
        while True:
            self.view.display_registered_players(self.tournament.players)
            player = player_controller.search_player()
            if player:
                self.tournament.players.append(player)
            else:
                break
        self.save()

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

    def run_tournament(self, round_controller, match_controller):
        if self.check_runnable():
            self.set_players_points(self.tournament)
            round_controller.previous_rounds = self.tournament.rounds
            while self.tournament.current_round <= self.tournament.number_rounds:
                round = round_controller.create_round(self.tournament.current_round)
                if self.tournament.current_round == 1:
                    shuffle(self.tournament.players)
                else:
                    self.tournament.players = sorted(
                        self.tournament.players, key=lambda p: p.points, reverse=True
                    )
                pairs = round_controller.pair_players(self.tournament.players)
                round.matchs = round_controller.run_round(pairs, round, match_controller)
                self.tournament.rounds.append(round)
                self.reset_players(pairs)
                self.tournament.current_round += 1
                if self.tournament.current_round > self.tournament.number_rounds:
                    description = self.view.input_tournament_description()
                    self.tournament.description = description
                self.save()

    def set_players_points(self, tournament):
        for round in tournament.rounds:
            for match in round.matchs:
                match.p1.points += match.s1
                match.p2.points += match.s2

    def reset_players(self, pairs):
        for pair in pairs:
            self.tournament.players.append(pair[0])
            self.tournament.players.append(pair[1])

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
