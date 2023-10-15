from os import listdir
from json import load


class ReportController:
    def __init__(self, view):
        self.view = view

    def run(self):
        running_report = True
        while running_report:
            self.view.display_menu()
            choice = self.view.select_menu()
            if choice == '1':
                all_players_data = self.extract_json_files_data("players")
                all_players_by_name = sorted(
                    all_players_data,
                    key=lambda p: p["first_name"]
                )
                self.view.list_players(all_players_by_name)
            elif choice == '2':
                all_tournaments_data = self.extract_json_files_data("tournaments")
                running_tournaments_list = True
                while running_tournaments_list:
                    self.view.all_tournaments_list(all_tournaments_data)
                    choice = self.view.select_menu()
                    if choice.isdigit() and int(choice) in range(1, len(all_tournaments_data)+1):
                        tournament_data = all_tournaments_data[int(choice) - 1]
                        running_tournament_info = True
                        while running_tournament_info:
                            self.view.tournament_menu(tournament_data)
                            choice = self.view.select_menu()
                            if choice == '1':
                                tournament_players = tournament_data["players"]
                                tournament_players_by_name = sorted(
                                    tournament_players,
                                    key=lambda p: p["first_name"]
                                )
                                self.view.list_players(tournament_players_by_name)
                            elif choice == '2':
                                tournament_rounds = tournament_data["rounds"]
                                self.view.list_rounds(tournament_rounds)
                            elif choice.upper() == 'X':
                                running_tournament_info = False
                            else:
                                self.view.alert_unknown_choice()
                    elif choice.upper() == 'X':
                        running_tournaments_list = False
                    else:
                        self.view.alert_unknown_choice()
            elif choice.upper() == 'X':
                running_report = False
            else:
                self.view.alert_unknown_choice()

    def extract_json_files_data(self, data_dir):
        json_files_data = []
        dir_path = f"data/{data_dir}/"
        files_names = listdir(dir_path)
        for file in files_names:
            file_path = f"{dir_path}{file}"
            with open(file_path, 'r', encoding='utf-8') as fp:
                file_data = load(fp)
                json_files_data.append(file_data)
        return json_files_data
