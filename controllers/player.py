from models.player import PlayerModel
from utils import save_json, list_data_files, extract_json, PLAYERS_DIR

class PlayerController:
    def __init__(self, view):
        self.view = view

    def create_player(self):
        player_data = self.view.input_player_data()
        player = PlayerModel.deserialize(player_data)
        file_path = f"{PLAYERS_DIR}{player.id}.json"
        save_json(player.serialize(), file_path)

    def search_player(self):
        id = self.view.input_player_id()
        players_files = list_data_files(PLAYERS_DIR)
        if f"{id}.json" in players_files:
            file_path = f"{PLAYERS_DIR}{id}.json"
            player_data = extract_json(file_path)
            player = PlayerModel.deserialize(player_data)
            self.view.display_player(player)
        else:
            self.view.alert_not_existing(id)