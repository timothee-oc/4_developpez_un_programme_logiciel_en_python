class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0
        self.affrontes = []

    def __str__(self):
        return f"{self.nom} {self.points}"
