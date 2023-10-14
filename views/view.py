class View:
    def display_main_menu(self):
        print()
        print("[MENU PRINCIPAL]")
        print(" 1 Créer un nouveau tournoi")
        print(" 2 Créer un nouveau joueur")
        print(" X Quitter")
        print()

    def select_main_menu(self):
        choice = input("Tapez le numéro de votre choix (ou X): ")
        print()
        return choice
    
    def input_player_data(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        date_of_birth = input("Date de naissance: ")
        player_id = input("Identifiant national: ")
        return {"first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "player_id": player_id}
    
    def alert_unknown_choice(self):
        print("Ce numéro ne correspond à aucune action. Réessayez.\n")

    def display_ranking(self, players):
        for player in players:
            print(player, player.points)
        print()