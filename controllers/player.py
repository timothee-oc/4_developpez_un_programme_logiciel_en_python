import re
from models import PlayerModel
from utils import list_data_files, extract_json, PLAYERS_DIR


class PlayerController:
    """
    Class that handles player related actions.
    """
    def __init__(self, player_view):
        self.view = player_view
        self.player = None

    def create_player(self):
        """
        Create a new player in the database from data input by the user.
        """
        player_data = self.view.input_player_data()
        self.player = PlayerModel(**player_data)
        if self.check_valid_id():
            self.player.save()
            self.view.inform_created()

    def check_valid_id(self):
        """
        Check is the ID provided by the user when creating a new player is valid.
        Valid means it is composed of two capital letters followed by 5 digits.
        It also must not be already existing in database.
        """
        players_files = list_data_files(PLAYERS_DIR)
        pattern = re.compile(r'^[A-Z]{2}\d{5}$')
        if not pattern.match(self.player.id_):
            self.view.alert_invalid_id(self.player.id_)
            return False
        if f"{self.player.id_}.json" in players_files:
            self.view.alert_already_existing(self.player.id_)
            return False
        return True

    def search_player(self):
        """
        Ask the user for a player id and search corresponding file in the database.
        If found, a player object is created as an attribute if this controller.
        Used for registration of players in tournaments.
        """
        players_files = list_data_files(PLAYERS_DIR)
        while True:
            id_ = self.view.input_player_id()
            if f"{id}.json" in players_files:
                file_path = f"{PLAYERS_DIR}{id}.json"
                player_data = extract_json(file_path)
                self.player = PlayerModel.deserialize(player_data)
                break
            elif id_ == "":
                self.player = None
                break
            else:
                self.view.alert_not_existing(id)

    def list_all_players(self):
        """
        Allows to generate a report displaying the full list of players
        in database ordered alphabetically.
        Also used during registration to inform the user of existing players IDs.
        """
        all_players_files = list_data_files(PLAYERS_DIR)
        all_players_data = [
            extract_json(f"{PLAYERS_DIR}{player_file}") for player_file in all_players_files
        ]
        all_players = [PlayerModel.deserialize(player_data) for player_data in all_players_data]
        all_players_ordered = sorted(all_players, key=lambda p: p.last_name)
        self.view.display_all_players(all_players_ordered)
