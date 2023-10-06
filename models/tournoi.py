from tour import Tour
from match import Match
from joueur import Joueur
import json
from random import shuffle


PATH_TO_JSON = "data/tournaments/tournoi.json"


class Tournoi:
    def __init__(self, joueurs, nombre_tours=4):
        self.nombre_tours = nombre_tours
        self.tour_actuel = 0
        self.tours = []
        self.joueurs = joueurs

    def run(self):
        for i in range(self.nombre_tours):
            self.tour_actuel = str(i + 1)
            if self.tour_actuel == '1':
                shuffle(self.joueurs)
            else:
                self.trier_par_score()
            paires_joueurs = self.associer_joueurs()
            print("\n")
            matchs = [Match(paire).play() for paire in paires_joueurs]
            tour = Tour(matchs, "Round " + self.tour_actuel)
            self.tours.append(tour)
            print("\n")
        for joueur in self.joueurs:
            print(joueur.prenom, joueur.points)

    def associer_joueurs(self):
        paires_joueurs = []
        for i in range(0, len(self.joueurs), 2):
            paires_joueurs.append((self.joueurs[i], self.joueurs[i+1]))
        return paires_joueurs

    def trier_par_score(self):
        self.joueurs = sorted(self.joueurs,
                              key=lambda joueur: joueur.points,
                              reverse=True)
        for joueur in self.joueurs:
            print(joueur.prenom, joueur.points)


with open(PATH_TO_JSON, 'r', encoding='utf-8') as json_tournoi:
    donnees_json = json.load(json_tournoi)

joueurs = [Joueur(joueur) for joueur in donnees_json["joueurs"]]
print([joueur.prenom for joueur in joueurs])
tournoi1 = Tournoi(joueurs)
tournoi1.run()
