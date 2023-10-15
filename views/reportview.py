from .mainview import MainView


class ReportView(MainView):
    def display_menu(self):
        print()
        print("[MENU DE RAPPORTS]")
        print(" 1 Liste de tous les joueurs")
        print(" 2 Liste de tous les tournois")
        print(" X Retour au menu principal")
        print()

    def list_players(self, players):
        for player in players:
            print(f"{player['first_name']} {player['last_name']}")
        print()

    def all_tournaments_list(self, tournaments):
        for i, tournament in enumerate(tournaments):
            print(f" {str(i+1)} {tournament['name']}")
        print(" X Retour au menu de rapports")
        print()

    def tournament_menu(self, tournament):
        print(f"{tournament['name']}")
        print(f"Du {tournament['start_date']} au {tournament['end_date']}")
        print(" 1 Liste des joueurs du tournoi")
        print(" 2 Liste des tours du tournoi")
        print(" X Retour à la liste des tournois")
        print()

    def list_rounds(self, rounds):
        for round in rounds:
            print(round["name"])
            for match in round["matchs"]:
                player1 = match[0][0]
                score1 = match[0][1]
                player2 = match[1][0]
                score2 = match[1][1]
                print(f"{player1['first_name']} {player1['last_name']} "
                      f"{score1} - {score2} "
                      f"{player2['first_name']} {player2['last_name']}")
            print()