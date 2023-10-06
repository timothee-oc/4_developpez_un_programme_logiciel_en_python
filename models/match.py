from random import choice


class Match:
    def __init__(self, paire_joueurs):
        self.joueur1 = paire_joueurs[0]
        self.joueur2 = paire_joueurs[1]

    def play(self):
        print(self.joueur1.prenom, self.joueur2.prenom)
        score1 = choice([0, 0.5, 1])
        score2 = 1 - score1
        self.joueur1.points += score1
        self.joueur2.points += score2
        return ([self.joueur1, score1], [self.joueur2, score2])
