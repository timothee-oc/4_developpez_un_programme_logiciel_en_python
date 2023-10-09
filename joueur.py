class Joueur:
    def __init__(self, nom, prenom, naissance):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.points = 0
        self.affrontes = []

    def __str__(self):
        return f"{self.prenom} {self.points}"
