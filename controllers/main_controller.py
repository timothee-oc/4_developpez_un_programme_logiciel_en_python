class MainController():
    def __init__(self, match_controller, player_controller,
                 report_controller, round_controller, tournament_controller,
                 main_view):
        self.match_controller = match_controller
        self.player_controller = player_controller
        self.report_controller = report_controller
        self.round_controller = round_controller
        self.tournament_controller = tournament_controller
        self.view = main_view

    def main_menu(self):
        while True:
            choice = self.view.choice_main()
            if choice == '1':
                self.tournament_menu()
            elif choice == '2':
                self.player_controller.create_player()
            elif choice == '3':
                self.report_menu()
            elif choice == '4':
                break
            else:
                self.view.alert_unknown_choice(choice)

    def tournament_menu(self):
        while True:
            choice = self.view.choice_tournament()
            if choice == '1':
                self.tournament_controller.create_tournament()
            elif choice == '2':
                self.tournament_controller.search_tournament()
                if self.tournament_controller.tournament:
                    self.tournament_controller.register_players(self.player_controller)
            elif choice == '3':
                self.tournament_controller.search_tournament()
                if self.tournament_controller.tournament:
                    self.tournament_controller.run_tournament(self.round_controller,
                                                              self.match_controller)
            elif choice == '4':
                break
            else:
                self.view.alert_unknown_choice(choice)

    def report_menu(self):
        while True:
            choice = self.view.choice_report()
            if choice == '1':
                self.player_controller.list_all_players()
            elif choice == '2':
                self.tournament_controller.list_all_tournaments()
            elif choice == '3':
                self.tournament_controller.display_one_tournament()
            elif choice == '4':
                self.tournament_controller.list_tournament_players()
            elif choice == '5':
                self.tournament_controller.list_tournament_rounds()
            elif choice == '6':
                break
            else:
                self.view.alert_unknown_choice(choice)