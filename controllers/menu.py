from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.report import ReportController
from views.tournament import TournamentView
from views.player import PlayerView
from views.report import ReportView

class MenuController:
    def __init__(self, view):
        self.view = view

    def process_choice(self):
        while True:
            choice = self.view.choice_main()
            if choice == '1':
                tournament_controller = TournamentController(view=TournamentView())
                while True:
                    choice = self.view.choice_tournament()
                    if choice == '1':
                        tournament_controller.create_tournament()
                    elif choice == '2':
                        tournament_controller.launch_tournament()
                    elif choice == '3':
                        break
                    else:
                        self.view.alert_unknown_choice(choice)
            elif choice == '2':
                player_controller = PlayerController(view=PlayerView())
                player_controller.create_player()
            elif choice == '3':
                report_controller = ReportController(view=ReportView())
                while True:
                    choice = self.view.choice_report()
                    if choice == '1':
                        report_controller.list_all_players()
                    elif choice == '2':
                        report_controller.list_all_tournaments()
                    elif choice == '3':
                        report_controller.display_one_tournament()
                    elif choice == '4':
                        report_controller.list_tournament_players()
                    elif choice == '5':
                        report_controller.list_tournament_rounds()
                    elif choice == '6':
                        break
                    else:
                        self.view.alert_unknown_choice(choice)
            elif choice == '4':
                break
            else:
                self.view.alert_unknown_choice(choice)