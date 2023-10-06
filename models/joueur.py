class Joueur:
    def __init__(self, joueur):
        self.nom_de_famille = joueur["nom_de_famille"]
        self.prenom = joueur["prenom"]
        self.date_de_naissance = joueur["date_de_naissance"]
        self.points = 0
