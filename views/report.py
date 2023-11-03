class ReportView:
    def display_all_players(self, players):
        print("LISTE DE TOUS LES JOUEURS:")
        for player in players:
            print(player)
            print()

    def display_all_tournaments(self, tournaments):
        print("LISTE DE TOUS LES TOURNOIS:")
        for tournament in tournaments:
            print(tournament)
            print()

    def input_tournament_name(self):
        name = input("Nom du tournoi: ")
        print()
        return name
    
    def alert_not_existing_tournament(self, name):
        print(f"Aucun tournoi ne correspond au nom {name} !\n")

    def display_tournament(self, tournament):
        print(tournament)
        print()

    def display_tournament_players(self, tournament):
        print(f"[JOUEURS INSCRITS AU TOURNOI '{tournament.name}']:")
        for player in tournament.players:
            print(player)
        print()

    def display_tournament_rounds(self, tournament):
        print(f"[ROUNDS DU TOURNOI '{tournament.name}']:")
        for round in tournament.rounds:
            print(f"\t{round}")
            for match in round.matchs:
                print(f"\t{match}")
            print()