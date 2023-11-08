class TournamentView:
    def input_tournament_data(self):
        tournament_data = {}
        tournament_data["name"] = input("Nom du tournoi: ")
        tournament_data["place"] = input("Lieu du tournoi: ")
        tournament_data["start_date"] = input("Date de début: ")
        tournament_data["end_date"] = input("Date de fin: ")
        print()
        return tournament_data
    
    def inform_created(self):
        print("Tournoi ajouté avec succès à la base de données !\n")
    
    def input_tournament_name(self):
        name = input("Nom du tournoi: ")
        print()
        return name
    
    def alert_not_existing_tournament(self, name):
        print(f"Aucun tournoi ne correspond au nom {name} !\n")

    def alert_already_finished(self):
        print(f"Tous les rounds de ce tournoi ont déjà été joués !\n")

    def display_registered_players(self, players):
        print(f"{len(players)} JOUEURS INSCRITS:\n")
        for player in players:
            print(f"\t{player.id}: {player.first_name} {player.last_name}")
        print()

    def alert_not_even(self):
        print(f"Vous devez inscrire un nombre pair de joueurs !\n")

    def alert_no_players(self):
        print(f"Vous devez inscrire au moins deux joueurs !\n")

    def display_all_tournaments(self, all_tournaments):
        print("[LISTE DE TOUS LES TOURNOIS]\n")
        for tournament in all_tournaments:
            print(tournament)
        print()

    def display_one_tournament(self, tournament):
        print(tournament)
        print()

    def display_tournament_players(self, tournament):
        print(f"[LISTE DES JOUEURS DU TOURNOI '{tournament.name}']\n")
        for player in tournament.players:
            print(player)
        print()

    def display_tournament_rounds(self, tournament):
        print(f"[LISTE DES ROUNDS DU TOURNOI '{tournament.name}']\n")
        for round in tournament.rounds:
            print(f"\t{round}")
            for match in round.matchs:
                print(f"\t{match}")
            print()
        print()