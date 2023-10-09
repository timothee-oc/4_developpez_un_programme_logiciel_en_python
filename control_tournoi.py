from tournoi import Tournoi
from tour import Tour
from match import Match
from vue_tournoi import VueTournoi
from random import shuffle, choice


class ControlTournoi:
    def __init__(self, joueurs):
        self.vue_tournoi = VueTournoi()
        self.tournoi = Tournoi(joueurs)

    def lancer_tournoi(self):
        shuffle(self.tournoi.joueurs)
        while self.tournoi.tour_actuel <= self.tournoi.nombre_tours:
            tour = Tour(f"Round {self.tournoi.tour_actuel}")
            print("\n")
            print(self.tournoi.tour_actuel)
            paires_joueurs = self.associer_joueurs()
            for paire in paires_joueurs:
                match = Match(paire[0], paire[1])
                match.joueur1.points += match.score1
                match.joueur2.points += match.score2
                match.joueur1.affrontes.append(match.joueur2)
                match.joueur2.affrontes.append(match.joueur1)
                tour.matchs.append(match)
            self.tournoi.tours.append(tour)
            self.tournoi.tour_actuel += 1
            self.tournoi.joueurs = self.classer_par_points(
                self.tournoi.joueurs
            )
            self.vue_tournoi.afficher_classement(self.tournoi.joueurs)

    def classer_par_points(self, joueurs):
        classement = sorted(
            joueurs,
            key=lambda j: j.points,
            reverse=True
        )
        return classement

    def associer_joueurs(self):
        paires_joueurs = []
        joueurs = self.tournoi.joueurs.copy()
        while len(joueurs) >= 2:
            j1 = joueurs.pop(0)
            j2 = self.trouver_paire(j1, joueurs)
            paires_joueurs.append((j1, j2))
            joueurs = self.classer_par_points(joueurs)
        return paires_joueurs

    def trouver_paire(self, j1, reste):
        j2 = reste.pop(0)
        if len(reste) != 0:
            while j2 in j1.affrontes:
                reste.append(j2)
                j2 = reste.pop(0)
            if self.meme_points_pas_affronte(j1, j2, reste[0]):
                candidats = self.trouver_candidats(j1, j2, reste)
                j2 = self.choisir_candidat(j2, candidats, reste)
        return j2

    def meme_points_pas_affronte(self, j1, j2, suivant):
        if suivant.points == j2.points and suivant not in j1.affrontes:
            return True
        else:
            return False

    def trouver_candidats(self, j1, j2, reste):
        candidats = [j2, reste[0]]
        for joueur in reste[1:]:
            if joueur.points != j2.points:
                break
            elif joueur in j1.affrontes:
                continue
            else:
                candidats.append(joueur)
        return candidats

    def choisir_candidat(self, j2, candidats, reste):
        choisi = choice(candidats)
        if choisi != j2:
            reste.append(j2)
            j2 = reste.pop(reste.index(choisi))
        return j2
