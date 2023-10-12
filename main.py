import json
from tournament import Tournament
from player import Player


def input_player_data():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    date_of_birth = input("Date of birth: ")
    player_id = input("Chess player ID: ")
    return {"first_name": first_name, "last_name": last_name,
            "date_of_birth": date_of_birth, "player_id": player_id}


def save_data(data, data_dir, file_name):
    file_path = f"data/{data_dir}/{file_name}.json"
    with open(file_path, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)


def main():
    # player_data = input_player_data()
    # save_data(player_data, "players", player_data['player_id'])
    tournament = Tournament("TOURNAMENT_NAME", "TOURNAMENT_PLACE")
    tournament.players = players
    tournament.run()


if __name__ == '__main__':
    players = [
        Player("Timothée", "Bachy", "05-07-1997", "AB12345"),
        Player("Pedro", "Gonzalez", "01-01-2001", "ZY98765"),
        Player("Marie", "Martin", "02-02-2002", "CD23456"),
        Player("Jean", "Bernard", "03-03-2003", "EF34567"),
        Player("Jeanne", "Thomas", "04-04-2004", "GH45678"),
        Player("Pierre", "Petit", "05-05-2005", "IJ56789"),
    ]
    main()
