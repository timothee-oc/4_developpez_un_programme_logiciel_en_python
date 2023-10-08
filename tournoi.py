class Tournoi:
    def __init__(self, joueurs, nombre_tours=4):
        self.joueurs = joueurs
        self.nombre_tours = nombre_tours
        self.tours = []
        self.tour_actuel = 1

    def afficher_joueurs(self):
        for joueur in self.joueurs:
            print(joueur)

    def afficher_classement(self):
        classement = sorted(self.joueurs, key=lambda j: j.points, reverse=True)
        for j in classement:
            print(j)
