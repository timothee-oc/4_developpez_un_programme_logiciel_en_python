from models.tournament import TournamentModel
from models.player import PlayerModel
from controllers.round import RoundController
from views.round import RoundView
from utils import TOURNAMENTS_DIR, PLAYERS_DIR, save_json, extract_json, list_data_files

class TournamentController:
    def __init__(self, view):
        self.view = view

    def create_tournament(self):
        tournament_data = self.view.input_tournament_data()
        tournament = TournamentModel(**tournament_data)
        file_path = f"{TOURNAMENTS_DIR}{tournament.name}.json"
        save_json(tournament.serialize(), file_path)

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
        while True:
            self.view.display_registered_players(tournament.players)
            id = self.view.input_player_id()
            if f"{id}.json" in list_data_files(PLAYERS_DIR):
                file_path = f"{PLAYERS_DIR}{id}.json"
                player_data = extract_json(file_path)
                player = PlayerModel.deserialize(player_data)
                tournament.players.append(player)
            elif id == 'x':
                if len(tournament.players) % 2 == 0:
                    break
                else:
                    self.view.alert_not_even()
            else:
                self.view.alert_not_existing_player(id)

    def run_tournament(self, tournament, file_path):
        if tournament.current_round > tournament.number_rounds:
            self.view.alert_already_finished()
        else:
            self.set_players_points(tournament)
            round_controller = RoundController(view=RoundView())
            while tournament.current_round <= tournament.number_rounds:
                round = round_controller.create_round(tournament)
                pairs = round_controller.pair_players(tournament)
                round.matchs = round_controller.run_round(pairs)
                tournament.rounds.append(round)
                tournament.reset_players(round)
                tournament.current_round += 1
                save_json(tournament.serialize(), file_path)

    def set_players_points(self, tournament):
        for round in tournament.rounds:
            for match in round.matchs:
                match.p1.points += match.s1
                match.p2.points += match.s2