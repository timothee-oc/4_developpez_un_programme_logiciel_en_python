class TournamentView:
    def display_ranking(self, tournament):
        tournament.sort_by_points()
        for player in tournament.players:
            print(player, player.points)
        print()