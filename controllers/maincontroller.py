from json import dump
from .tournamentcontroller import TournamentController
from .usercontroller import UserController
from .reportcontroller import ReportController
from views.tournamentview import TournamentView
from views.userview import UserView
from views.reportview import ReportView


class MainController:
    def __init__(self, view):
        self.view = view
    
    def run(self):
        running_main = True
        while running_main:
            self.view.display_menu()
            choice = self.view.select_menu()
            if choice == '1':
                tournament_view = TournamentView()
                tournament_controller = TournamentController(tournament_view)
                tournament = tournament_controller.run()
                self.save_data(tournament.serialize(), "tournaments", tournament.name)
            elif choice == '2':
                user_view = UserView()
                user_controller = UserController(user_view)
                player_data = user_controller.run()
                self.save_data(player_data, "players", player_data["player_id"])
            elif choice == '3':
                report_view = ReportView()
                report_controller = ReportController(report_view)
                report_controller.run()
            elif choice.upper() == 'X':
                running_main = False
            else:
                self.view.alert_unknown_choice()

    def save_data(self, data, data_dir, file_name):
        file_path = f"data/{data_dir}/{file_name}.json"
        with open(file_path, 'w', encoding='utf-8') as fp:
            dump(data, fp, ensure_ascii=False, indent=4)
