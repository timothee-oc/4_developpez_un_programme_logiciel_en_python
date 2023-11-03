from models.player import PlayerModel
from models.tournament import TournamentModel
from utils import list_data_files, extract_json, PLAYERS_DIR, TOURNAMENTS_DIR

class ReportController:
    def __init__(self, view):
        self.view = view

    def list_all_players(self):
        all_players_files = list_data_files(PLAYERS_DIR)
        all_players_data = [
            extract_json(f"{PLAYERS_DIR}{player_file}") for player_file in all_players_files
        ]
        all_players = [
            PlayerModel.deserialize(player_data) for player_data in all_players_data
        ]
        self.view.display_all_players(all_players)

    def list_all_tournaments(self):
        all_tournaments_files = list_data_files(TOURNAMENTS_DIR)
        all_tournaments_data = [
            extract_json(f"{TOURNAMENTS_DIR}{tournament_file}") for tournament_file in all_tournaments_files
        ]
        all_tournaments = [
            TournamentModel.deserialize(tournament_data) for tournament_data in all_tournaments_data
        ]
        self.view.display_all_tournaments(all_tournaments)

    def display_one_tournament(self):
        name = self.view.input_tournament_name()
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        if f"{name}.json" in tournaments_files:
            file_path = f"{TOURNAMENTS_DIR}{name}.json"
            tournament_data = extract_json(file_path)
            tournament = TournamentModel.deserialize(tournament_data)
            self.view.display_tournament(tournament)
        else:
            self.view.alert_not_existing_tournament(name)
            return None
        
    def list_tournament_players(self):
        name = self.view.input_tournament_name()
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        if f"{name}.json" in tournaments_files:
            file_path = f"{TOURNAMENTS_DIR}{name}.json"
            tournament_data = extract_json(file_path)
            tournament = TournamentModel.deserialize(tournament_data)
            self.view.display_tournament_players(tournament)
        else:
            self.view.alert_not_existing_tournament(name)
            return None
        
    def list_tournament_rounds(self):
        name = self.view.input_tournament_name()
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        if f"{name}.json" in tournaments_files:
            file_path = f"{TOURNAMENTS_DIR}{name}.json"
            tournament_data = extract_json(file_path)
            tournament = TournamentModel.deserialize(tournament_data)
            self.view.display_tournament_rounds(tournament)
        else:
            self.view.alert_not_existing_tournament(name)
            return None