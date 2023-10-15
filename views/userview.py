class UserView:
    def input_player_data(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        date_of_birth = input("Date de naissance: ")
        player_id = input("Identifiant national: ")
        return {"first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "player_id": player_id}