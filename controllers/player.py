from models import PlayerModel
from utils import list_data_files, extract_json, PLAYERS_DIR


class PlayerController:
    def __init__(self, player_view):
        self.view = player_view
        self.player = None

    def create_player(self):
        player_data = self.view.input_player_data()
        self.player = PlayerModel(**player_data)
        self.player.save()
        self.view.inform_created()

    def search_player(self):
        players_files = list_data_files(PLAYERS_DIR)
        while True:
            id = self.view.input_player_id()
            if f"{id}.json" in players_files:
                file_path = f"{PLAYERS_DIR}{id}.json"
                player_data = extract_json(file_path)
                self.player = PlayerModel.deserialize(player_data)
                break
            elif id == "":
                self.player = None
                break
            else:
                self.view.alert_not_existing(id)

    def list_all_players(self):
        all_players_files = list_data_files(PLAYERS_DIR)
        all_players_data = [extract_json(f"{PLAYERS_DIR}{player_file}") for player_file in all_players_files]
        all_players = [PlayerModel.deserialize(player_data) for player_data in all_players_data]
        self.view.display_all_players(all_players)
