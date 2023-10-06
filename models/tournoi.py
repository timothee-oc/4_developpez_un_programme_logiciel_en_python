from models.tour import Tour
from models.match import Match
from random import shuffle


class Tournoi:
    def __init__(self, joueurs, nombre_tours=4):
        self.nombre_tours = nombre_tours
        self.tour_actuel = 0
        self.tours = []
        self.joueurs = joueurs

    def run(self):
        for i in range(self.nombre_tours):
            self.tour_actuel = str(i + 1)
            self.trier_par_score()
            paires_joueurs = self.associer_joueurs()
            matchs = [Match(paire).play() for paire in paires_joueurs]
            tour = Tour(matchs, "Round " + self.tour_actuel)
            self.tours.append(tour)
        self.trier_par_score()

    def associer_joueurs(self):
        paires_joueurs = []
        for i in range(0, len(self.joueurs), 2):
            paires_joueurs.append((self.joueurs[i], self.joueurs[i+1]))
        return paires_joueurs

    def trier_par_score(self):
        if self.tour_actuel == '1':
            shuffle(self.joueurs)
        else:
            self.joueurs = sorted(self.joueurs,
                                  key=lambda joueur: joueur.points,
                                  reverse=True)
        for joueur in self.joueurs:
            print(joueur.prenom, joueur.points)
