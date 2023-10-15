class UserController:
    def __init__(self, view):
        self.view = view

    def run(self):
        player_data = self.view.input_player_data()
        return player_data