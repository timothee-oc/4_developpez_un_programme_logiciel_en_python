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
        print("Tous les rounds de ce tournoi ont déjà été joués !\n")

    def display_registered_players(self, players):
        print(f"{len(players)} JOUEURS INSCRITS:\n")
        for player in players:
            print(f"\t{player.id}: {player.first_name} {player.last_name}")
        print()

    def alert_not_even(self):
        print("Vous devez inscrire un nombre pair de joueurs !\n")

    def alert_no_players(self):
        print("Vous devez inscrire au moins deux joueurs !\n")

    def display_all_tournaments(self, all_tournaments):
        print("[LISTE DE TOUS LES TOURNOIS]\n")
        for tournament in all_tournaments:
            print(f"{tournament.name}")
        print()

    def display_one_tournament(self, tournament):
        print(
            f"{tournament.name}\n"
            f"Lieu: {tournament.place}\n"
            f"Du {tournament.start_date} au {tournament.end_date}\n"
        )

    def display_tournament_players(self, tournament):
        print(f"[LISTE DES JOUEURS DU TOURNOI '{tournament.name}']\n")
        for player in tournament.players:
            print(f"{player.first_name} {player.last_name}")
        print()

    def display_tournament_rounds(self, tournament):
        print(f"[LISTE DES ROUNDS DU TOURNOI '{tournament.name}']\n")
        for round in tournament.rounds:
            print(
                f"\t{round.name}\n"
                f"\t{round.start_date_time.strftime('Commencé le %d/%m/%Y à %H:%M:%S')}"
            )
            for match in round.matchs:
                print(
                    f"\t\t{match.p1.first_name} {match.p1.last_name} "
                    f"{match.s1} - {match.s2} "
                    f"{match.p2.first_name} {match.p2.last_name}"
                )
            print()
        print()

    def input_tournament_description(self):
        print("Entrez une description du tournoi: ")
        description = input("=> ")
        print()
        return description
