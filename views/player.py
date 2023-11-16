class PlayerView:
    def input_player_data(self):
        player_data = {}
        player_data["first_name"] = input("Prénom: ")
        player_data["last_name"] = input("Nom de famille: ")
        player_data["birth_date"] = input("Date de naissance: ")
        player_data["id"] = input("Identifiant national: ")
        print()
        return player_data

    def input_player_id(self):
        id = input("Identifiant du joueur: ")
        print()
        return id

    def alert_not_existing(self, id):
        print(f"Aucun joueur ne correspond à l'identifiant {id} !\n")

    def inform_created(self):
        print("Joueur ajouté avec succès à la base de données !\n")

    def display_all_players(self, all_players):
        print("[LISTE DE TOUS LES JOUEURS]\n")
        for player in all_players:
            print(
                f"{player.first_name} {player.last_name}\n"
                f"Né(e) le {player.birth_date}\n"
                f"INE: {player.id}\n"
            )
