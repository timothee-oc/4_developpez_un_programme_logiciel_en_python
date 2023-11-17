class PlayerView:
    """
    View class associated with the PlayerController class.
    Used for various actions related to players handling.
    """
    def input_player_data(self):
        """
        Ask user to input player data when creating a new player in database.

        :return player_data(dict)
        """
        player_data = {}
        player_data["first_name"] = input("Prénom: ")
        player_data["last_name"] = input("Nom de famille: ")
        player_data["birth_date"] = input("Date de naissance: ")
        player_data["id"] = input("Identifiant national: ")
        print()
        return player_data

    def alert_invalid_id(self, id):
        """
        Alert the user that the provided ID for player creation is not a sequence of two capital letters
        and 5 digits.
        """
        print(f"Erreur: l'ID '{id}' n'est pas valide !")
        print("L'ID doit être composé de deux lettres majuscules suivies de cinq chiffres (par exemple, AB12345)\n")

    def alert_already_existing(self, id):
        """
        Tell the user that the player he is trying to create already exist in database.
        """
        print(f"Un joueur avec l'ID '{id}' existe déjà dans la base de données !\n")

    def input_player_id(self):
        """
        Ask the user to input a player ID.
        Used when registering a player to a tournament.

        :return id(string)
        """
        id = input("Identifiant du joueur: ")
        print()
        return id

    def alert_not_existing(self, id):
        """
        Tell the user that the player he is trying to register does not exist in database.
        """
        print(f"Aucun joueur ne correspond à l'identifiant {id} !\n")

    def inform_created(self):
        """
        Inform the user that the new player was succesfully created in database.
        """
        print("Joueur ajouté avec succès à la base de données !\n")

    def display_all_players(self, all_players):
        """
        Generates a report of all players existing in database with their personnal data.
        """
        print("[LISTE DE TOUS LES JOUEURS]\n")
        for player in all_players:
            print(
                f"{player.first_name} {player.last_name}\n"
                f"Né(e) le {player.birth_date}\n"
                f"INE: {player.id}\n"
            )
