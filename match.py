from random import choice


class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = choice([0, 0.5, 1])
        self.score2 = 1 - self.score1
        self.paire = ([self.joueur1, self.score1],
                      [self.joueur2, self.score2])
