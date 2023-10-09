import json
from joueur import Joueur
from control_tournoi import ControlTournoi


def lire_json():
    with open('joueurs.json', 'r', encoding='utf-8') as fj:
        joueurs = json.load(fj)
    return joueurs


def afficher_menu():
    print("Que voulez-vous faire ?\n")
    print("1. Créer un tournoi")
    print("2. Créer un joueur")
    print("X. Quitter")


def executer_choix(choix):
    if choix == '1':
        creer_tournoi()
    elif choix == '2':
        creer_joueur()
    else:
        print("Ce numéro ne correspond à aucune action")


def creer_tournoi():
    joueurs = [Joueur(**joueur) for joueur in JOUEURS[:6]]
    control_tournoi = ControlTournoi(joueurs)
    control_tournoi.lancer_tournoi()


def creer_joueur():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    naissance = input("Date de naissance : ")
    joueur = {
        "nom": nom,
        "prenom": prenom,
        "naissance": naissance
    }
    JOUEURS.append(joueur)
    with open('joueurs.json', 'w', encoding='utf-8') as fj:
        json.dump(JOUEURS, fj, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    JOUEURS = lire_json()
    while True:
        afficher_menu()
        choix = input("Entrez un numéro de 1 à 2 ou X: ")
        if choix == 'X':
            break
        else:
            executer_choix(choix)
