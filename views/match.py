class MatchView:
    def input_winner(self, match):
        print(f"{match.p1.first_name} vs {match.p2.first_name}")
        print("Qui a gagné ce match ?")
        winner = input(
            "0 -> Egalité\n"
            f"1 -> {match.p1.first_name}\n"
            f"2 -> {match.p2.first_name}\n"
            "=> "
            )
        print()
        return winner
