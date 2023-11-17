class TournamentView:
    """
    View class associated with the TournamentController class.
    Handles various actions related to tournaments.
    """
    def input_tournament_data(self):
        """
        Ask the user to input a new tournament's data when creating it in the database.

        :return tournament_data(dict)
        """
        tournament_data = {}
        tournament_data["name"] = input("Nom du tournoi: ")
        tournament_data["place"] = input("Lieu du tournoi: ")
        tournament_data["start_date"] = input("Date de début: ")
        tournament_data["end_date"] = input("Date de fin: ")
        print()
        return tournament_data

    def inform_created(self):
        """
        Inform the user that the new tournament was successfully created in database.
        """
        print("Tournoi ajouté avec succès à la base de données !\n")

    def input_tournament_name(self):
        """
        Ask the user to input a tournament name for searching it in the database.

        :return name(string)
        """
        name = input("Nom du tournoi: ")
        print()
        return name

    def alert_not_existing(self, name):
        """
        Alert the user that the tournament he is searching does not exist in database.
        """
        print(f"Aucun tournoi ne correspond au nom {name} !\n")

    def alert_already_finished(self):
        """
        Alert the user that the tournament he is trying to launch is already over.
        """
        print("Tous les rounds de ce tournoi ont déjà été joués !\n")

    def display_registered_players(self, players):
        """
        Displays a list of all the players already registered in a given tournament.
        """
        print(f"{len(players)} JOUEURS INSCRITS:\n")
        for player in players:
            print(f"\t{player.id}: {player.first_name} {player.last_name}")
        print()

    def alert_not_even(self):
        """
        Alert the user that a tournament cannot be launched with an odd number of players.
        """
        print("Vous devez inscrire un nombre pair de joueurs !\n")

    def alert_no_players(self):
        """
        Alert the user that a tournament cannot be launched with no registered players.
        """
        print("Vous devez inscrire au moins deux joueurs !\n")

    def display_all_tournaments(self, all_tournaments):
        """
        Generates a report of all existing tournaments in the database.
        """
        print("[LISTE DE TOUS LES TOURNOIS]\n")
        for tournament in all_tournaments:
            print(f"{tournament.name}")
        print()

    def display_one_tournament(self, tournament):
        """
        Generates a report of a given tournament's name, place and dates of start and finish
        """
        print(
            f"{tournament.name}\n"
            f"Lieu: {tournament.place}\n"
            f"Du {tournament.start_date} au {tournament.end_date}\n"
        )

    def display_tournament_players(self, tournament):
        """
        Generates a report of all registered players in a given tournament.
        """
        print(f"[LISTE DES JOUEURS DU TOURNOI '{tournament.name}']\n")
        for player in tournament.players:
            print(f"{player.first_name} {player.last_name}")
        print()

    def display_tournament_rounds(self, tournament):
        """
        Generates a report of all rounds of a given tournament and for each
        of its rounds displays all the matchs.
        """
        print(f"[LISTE DES ROUNDS DU TOURNOI '{tournament.name}']\n")
        for round in tournament.rounds:
            print(
                f"\t{round.name}\n"
                f"\t{round.start_date_time.strftime('Commencé le %d/%m/%Y à %H:%M:%S')}"
            )
            for match in round.matchs:
                print(
                    f"\t\t{match.player1.first_name} {match.player1.last_name} "
                    f"{match.score1} - {match.score2} "
                    f"{match.player2.first_name} {match.player2.last_name}"
                )
            if round.end_date_time:
                print(f"\t{round.end_date_time.strftime('Fini le %d/%m/%Y à %H:%M:%S')}\n")
            else:
                print("\tEn cours...\n")
        print()

    def display_round_matchs(self, round):
        """
        When playing a round, displays a list of the matchs of this round.
        """
        print(f"{round.name}\n")
        print("Matchs du round:")
        for match in round.matchs:
            print(f"\t{match.player1.first_name} vs {match.player2.first_name}")
        print()

    def input_winner(self, match):
        """
        When playing a match, ask the user to select a winner between the two players, or a draw.

        :return winner(string)
        """
        print(f"{match.player1.first_name} vs {match.player2.first_name}")
        print("Qui a gagné ce match ?")
        winner = input(
            "0 -> Egalité\n"
            f"1 -> {match.player1.first_name}\n"
            f"2 -> {match.player2.first_name}\n"
            "=> "
            )
        print()
        return winner
