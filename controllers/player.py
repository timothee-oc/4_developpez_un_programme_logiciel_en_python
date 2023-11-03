from models.player import PlayerModel
from utils import save_json, list_data_files, extract_json, PLAYERS_DIR

class PlayerController:
    def __init__(self, player_view):
        self.view = player_view

    def create_player(self):
        player_data = self.view.input_player_data()
        player = PlayerModel.deserialize(player_data)
        file_path = f"{PLAYERS_DIR}{player.id}.json"
        save_json(player.serialize(), file_path)
        self.view.inform_created()

    def search_player(self):
        while True:
            id = self.view.input_player_id()
            if f"{id}.json" in list_data_files(PLAYERS_DIR):
                file_path = f"{PLAYERS_DIR}{id}.json"
                player_data = extract_json(file_path)
                player = PlayerModel.deserialize(player_data)
                return player
            elif id == "":
                return None
            else:
                self.view.alert_not_existing(id)