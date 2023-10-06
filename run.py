from models.tournoi import Tournoi
from models.joueur import Joueur
import json

PATH_TO_JSON = "data/tournaments/tournoi.json"

with open(PATH_TO_JSON, 'r', encoding='utf-8') as json_tournoi:
    donnees_json = json.load(json_tournoi)

joueurs = [Joueur(joueur) for joueur in donnees_json["joueurs"]]
print([joueur.prenom for joueur in joueurs])
tournoi1 = Tournoi(joueurs)
tournoi1.run()
