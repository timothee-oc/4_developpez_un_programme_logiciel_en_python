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

    def display_player(self, player):
        print(player)