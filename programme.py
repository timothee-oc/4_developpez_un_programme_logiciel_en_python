from joueur import Joueur
from tournoi import Tournoi
from tour import Tour
from match import Match
from random import shuffle, choice

JOUEURS = [
    {"nom": "Marie"},
    {"nom": "Jean"},
    {"nom": "Jeanne"},
    {"nom": "Pierre"},
    {"nom": "Françoise"},
    {"nom": "Michel"}
]


def classer_par_points(joueurs):
    return sorted(joueurs, key=lambda j: j.points, reverse=True)


def choisir_candidat(joueur2, candidats, reste):
    choisi = choice(candidats)
    if choisi != joueur2:
        reste.append(joueur2)
        joueur2 = reste.pop(reste.index(choisi))
    return joueur2


def trouver_candidats(joueur1, joueur2, reste):
    candidats = [joueur2, reste[0]]
    for joueur in reste[1:]:
        if joueur.points != joueur2.points:
            break
        elif joueur in joueur1.affrontes:
            continue
        else:
            candidats.append(joueur)
    return candidats


def meme_points_pas_affronte(joueur1, joueur2, suivant):
    if suivant.points == joueur2.points and suivant not in joueur1.affrontes:
        return True
    else:
        return False


def trouver_paire(joueur1, reste):
    joueur2 = reste.pop(0)
    if len(reste) != 0:
        while joueur2 in joueur1.affrontes:
            reste.append(joueur2)
            joueur2 = reste.pop(0)
        if meme_points_pas_affronte(joueur1, joueur2, reste[0]):
            candidats = trouver_candidats(joueur1, joueur2, reste)
            joueur2 = choisir_candidat(joueur2, candidats, reste)
    return joueur2


def associer_joueurs(joueurs):
    paires_joueurs = []
    while len(joueurs) >= 2:
        joueur1 = joueurs.pop(0)
        joueur2 = trouver_paire(joueur1, joueurs)
        paires_joueurs.append((joueur1, joueur2))
        joueurs = classer_par_points(joueurs)
    return paires_joueurs


joueurs = [Joueur(**joueur) for joueur in JOUEURS]
tournoi = Tournoi(joueurs)
shuffle(joueurs)
while tournoi.tour_actuel <= tournoi.nombre_tours:
    tour = Tour(f"Round {tournoi.tour_actuel}")
    print("\n")
    print(tournoi.tour_actuel)
    joueurs = classer_par_points(joueurs)
    paires_joueurs = associer_joueurs(joueurs.copy())
    for paire in paires_joueurs:
        match = Match(paire[0], paire[1])
        match.joueur1.points += match.score1
        match.joueur2.points += match.score2
        match.joueur1.affrontes.append(match.joueur2)
        match.joueur2.affrontes.append(match.joueur1)
        tour.matchs.append(match)
    tournoi.tours.append(tour)
    tournoi.tour_actuel += 1
    tournoi.afficher_classement()
