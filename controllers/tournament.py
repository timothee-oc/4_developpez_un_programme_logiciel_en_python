from models.tournament import TournamentModel
from controllers.player import PlayerController
from views.player import PlayerView
from controllers.round import RoundController
from views.round import RoundView
from utils import TOURNAMENTS_DIR, save_json, extract_json, list_data_files
from random import shuffle

class TournamentController:
    def __init__(self, view):
        self.view = view

    def create_tournament(self):
        tournament_data = self.view.input_tournament_data()
        tournament = TournamentModel(**tournament_data)
        file_path = f"{TOURNAMENTS_DIR}{tournament.name}.json"
        save_json(tournament.serialize(), file_path)
        self.view.inform_created()

    def launch_tournament(self):
        tournament = self.search_tournament()
        if tournament:
            file_path = f"{TOURNAMENTS_DIR}{tournament.name}.json"
            if tournament.players == []:
                self.register_players(tournament)
                save_json(tournament.serialize(), file_path)
            self.run_tournament(tournament, file_path)

    def search_tournament(self):
        name = self.view.input_tournament_name()
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        if f"{name}.json" in tournaments_files:
            file_path = f"{TOURNAMENTS_DIR}{name}.json"
            tournament_data = extract_json(file_path)
            return TournamentModel.deserialize(tournament_data)
        else:
            self.view.alert_not_existing_tournament(name)
            return None
        
    def register_players(self, tournament):
        player_controller = PlayerController(PlayerView())
        while True:
            self.view.display_registered_players(tournament)
            player = player_controller.search_player()
            if player:
                tournament.players.append(player)
            else:
                if len(tournament.players) % 2 == 0:
                    break
                else:
                    self.view.alert_not_even()

    def run_tournament(self, tournament, file_path):
        if tournament.current_round > tournament.number_rounds:
            self.view.alert_already_finished()
        else:
            self.set_players_points(tournament)
            round_controller = RoundController(tournament.rounds, view=RoundView())
            while tournament.current_round <= tournament.number_rounds:
                round = round_controller.create_round(tournament.current_round)
                if tournament.current_round == 1:
                    shuffle(tournament.players)
                else:
                    tournament.players = sorted(
                        tournament.players, key=lambda p: p.points, reverse=True
                    )
                pairs = round_controller.pair_players(tournament.players)
                round.matchs = round_controller.run_round(pairs, round)
                tournament.rounds.append(round)
                self.reset_players(round, tournament)
                tournament.current_round += 1
                save_json(tournament.serialize(), file_path)

    def set_players_points(self, tournament):
        for round in tournament.rounds:
            for match in round.matchs:
                match.p1.points += match.s1
                match.p2.points += match.s2

    def reset_players(self, round, tournament):
        for match in round.matchs:
            tournament.players.append(match.p1)
            tournament.players.append(match.p2)