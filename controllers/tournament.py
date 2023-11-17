from models import TournamentModel, RoundModel, MatchModel
from utils import TOURNAMENTS_DIR, extract_json, list_data_files
from random import shuffle, choice
from datetime import datetime


class TournamentController:
    """
    Main class of the program that handles all the tournament logic.
    """
    def __init__(self, tournament_view):
        self.view = tournament_view
        self.tournament = None

    def create_tournament(self):
        """
        Create a new tournament in database from user input.
        """
        tournament_data = self.view.input_tournament_data()
        if self.check_number_rounds(tournament_data):
            self.tournament = TournamentModel(**tournament_data)
            if self.check_valid_name():
                self.tournament.save()
                self.view.inform_created()

    def check_number_rounds(self, tournament_data):
        """
        Check the user input for the number of rounds of the new tournament.
        If empty, we keep the default value number_rounds attribute.
        Input is valid if it can be cast to an integer >= 1
        """
        if tournament_data["number_rounds"] == "":
            del tournament_data["number_rounds"]
            return True

        if not tournament_data["number_rounds"].isdigit() or int(tournament_data["number_rounds"]) == 0:
            self.view.alert_not_int(tournament_data["number_rounds"])
            return False

        return True

    def check_valid_name(self):
        """
        Check if the name provided by the user when creating a new tournament is valid.
        Valid means it must not be already existing in database.

        :return bool
        """
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        if f"{self.tournament.name}.json" in tournaments_files:
            self.view.alert_already_existing(self.tournament.name)
            return False
        return True

    def search_tournament(self):
        """
        Ask the user for a tournament name and search its file in database.
        If found, instantiate the tournament attribute of this class as a
        tournament object.
        """
        tournaments_files = list_data_files(TOURNAMENTS_DIR)
        while True:
            name = self.view.input_tournament_name()
            if f"{name}.json" in tournaments_files:
                file_path = f"{TOURNAMENTS_DIR}{name}.json"
                tournament_data = extract_json(file_path)
                self.tournament = TournamentModel.deserialize(tournament_data)
                break
            elif name == '':
                self.tournament = None
                break
            else:
                self.view.alert_not_existing(name)

    def register_players(self, player_controller):
        """
        Allows the user to register one or more player(s) to an existing tournament.
        Uses the player controller to display players in database and search one among them.

        :params player_controller(PlayerController)
        """
        self.search_tournament()
        if self.tournament:
            player_controller.list_all_players()
            while True:
                self.view.display_registered_players(self.tournament.players)
                player_controller.search_player()
                if player_controller.player:
                    self.tournament.players.append(player_controller.player)
                else:
                    break
            self.tournament.save()

    def check_runnable(self):
        """
        Check if the tournament to be launched is runnable:
            - At least two registered players
            - Not an odd number of players
            - Still rounds to be played (not over)

        :return bool
        """
        if len(self.tournament.players) == 0:
            self.view.alert_no_players()
            return False
        if len(self.tournament.players) % 2 != 0:
            self.view.alert_not_even()
            return False
        if self.tournament.current_round > self.tournament.number_rounds:
            self.view.alert_already_finished()
            return False
        return True

    def update_players_points(self, match):
        """
        Update the points of a match's players in the tournament players list using their
        corresponding copy in a given match.
        Index can be retrieved because equality of player objects depends on ID attribute.
        """
        player1_index = self.tournament.players.index(match.player1)
        player2_index = self.tournament.players.index(match.player2)
        self.tournament.players[player1_index].points += match.score1
        self.tournament.players[player2_index].points += match.score2

    def set_players_points(self):
        """
        Set tournament's players points back to the amount they had when
        last exited the tournament.
        Done by going through all previous matchs of all previous rounds.
        Needed because points are not saved in player serialization.
        """
        for round in self.tournament.rounds:
            for match in round.matchs:
                self.update_players_points(match)

    def check_already_met(self, p1, candidate):
        """
        During pairs making, check if the current candidate has already met
        the player we are trying to make a pair with.
        Done by going through all previous matchs of previous rounds.

        :params p1(PlayerModel), candidate(PlayerModel)

        :return bool
        """
        for round in self.tournament.rounds:
            for match in round.matchs:
                if (match.player1, match.player2) in [(p1, candidate), (candidate, p1)]:
                    return True
        return False

    def find_candidates(self, p1, players):
        """
        Find a list of players allowed to play against the player we are trying to match.
        Candidates need to have the same number of points and to not have already
        met the p1.

        :params p1(PlayerModel)

        :return list[PlayerModel]
        """
        reference = players[0].points
        candidates = []
        for player in players:
            if player.points != reference:
                break
            elif not self.check_already_met(p1, player):
                candidates.append(player)
        return candidates

    def find_p2(self, p1, players):
        """
        Tries to find a second player to form a pair with the p1.
        If there's only one player left in the list, make a pair him/her.
        If the second to next has less points, make a pair with the next.
        If no candidates were found (all already met p1), make a pair with the next.
        Else choose a random candidate from the list.

        :params p1(PlayerModel)

        :return player(PlayerModel)
        """
        if len(players) > 1 and players[0].points == players[1].points:
            candidates = self.find_candidates(p1, players)
            if len(candidates) > 0:
                chosen = choice(candidates)
                chosen_index = players.index(chosen)
                return players.pop(chosen_index)
        return players.pop(0)

    def pair_players(self):
        """
        Make pairs of players before starting a new round.
        Begin with first player in the list (most points) and try to find
        the best match among next players using their points and checking
        if they have already met.

        :return list[tuple(player(PlayerModel), player(PlayerModel))]
        """
        players = self.tournament.players.copy()
        if self.tournament.current_round == 1:
            shuffle(players)
        else:
            players = sorted(players, key=lambda p: p.points, reverse=True)
        pairs = []
        while len(players) >= 2:
            p1 = players.pop(0)
            p2 = self.find_p2(p1, players)
            pairs.append((p1, p2))
        return pairs

    def run_match(self, match):
        """
        Run one of the matchs of a given round.
        Ask the user to select a winner between both players of a match.
        Set players scores (0 if looser, 1 if winner, 0.5 for both if draw).
        Update players points accordingly.

        :params match(MatchModel)
        """
        winner = self.view.input_winner(match)
        if winner == '1':
            match.score1 = 1
        elif winner == '2':
            match.score2 = 1
        else:
            match.score1 = match.score2 = 0.5
        self.update_players_points(match)

    def run_round(self):
        """
        Run a round of the tournament.
        Display the list of the round's matchs, and run matchs in order, after checking
        it hasn't already been played.
        Put back match's players in tournament players list to be paired again in next round.
        Save tournament sate after each match, allowing to exit program and start again where
        we left.
        """
        self.view.display_round_matchs(self.tournament.rounds[-1])
        for match in self.tournament.rounds[-1].matchs:
            if match.score1 == 0 and match.score2 == 0:
                self.run_match(match)
                self.tournament.save()

    def run_tournament(self):
        """
        Entry point of this class.
        Ask the user to select an existing tournament and check if it can be run.
        While there's still rounds to play, check if a round is currently being played
        or create the next one.
        Players are randomly shuffled before round 1, else sorted by points.
        Players are put in pairs and Match object created for each pair.
        Tournament state is also saved between rounds because we update round's end date and time
        as well as the tournament's current round number.
        """
        self.search_tournament()
        if self.tournament and self.check_runnable():
            self.set_players_points()
            while self.tournament.current_round <= self.tournament.number_rounds:
                if len(self.tournament.rounds) == 0 or self.tournament.rounds[-1].end_date_time:
                    self.tournament.rounds.append(
                        RoundModel(name=f"Round {self.tournament.current_round}", start_date_time=datetime.now())
                    )
                    pairs = self.pair_players()
                    self.tournament.rounds[-1].matchs = [MatchModel(([pair[0], 0], [pair[1], 0])) for pair in pairs]
                self.view.display_ranking(sorted(self.tournament.players, key=lambda p: p.points, reverse=True))
                self.run_round()
                self.tournament.rounds[-1].end_date_time = datetime.now()
                self.tournament.current_round += 1
                self.tournament.save()
            self.tournament.players = sorted(self.tournament.players, key=lambda p: p.points, reverse=True)
            self.view.inform_tournament_over(self.tournament)

    def list_all_tournaments(self):
        """
        Allows to generate a report of all the tournaments existing in the database.
        """
        all_tournaments_files = list_data_files(TOURNAMENTS_DIR)
        all_tournaments_data = [
            extract_json(f"{TOURNAMENTS_DIR}{tournament_file}") for tournament_file in all_tournaments_files
        ]
        all_tournaments = [TournamentModel.deserialize(tournament_data) for tournament_data in all_tournaments_data]
        self.view.display_all_tournaments(all_tournaments)

    def display_one_tournament(self):
        """
        Ask the user for a tournament's name and if found, display its dates and place.
        """
        self.search_tournament()
        if self.tournament:
            self.view.display_one_tournament(self.tournament)

    def list_tournament_players(self):
        """
        Ask the user for a tournament's name and if found, display its registered players.
        """
        self.search_tournament()
        if self.tournament:
            self.view.display_tournament_players(self.tournament)

    def list_tournament_rounds(self):
        """
        Ask the user for a tournament's name and if found, display its rounds and for each
        round its matchs.
        """
        self.search_tournament()
        if self.tournament:
            self.view.display_tournament_rounds(self.tournament)
