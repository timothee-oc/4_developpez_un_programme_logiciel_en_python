class Tournoi:
    def __init__(self, joueurs, nombre_tours=4):
        self.joueurs = joueurs
        self.nombre_tours = nombre_tours
        self.tours = []
        self.tour_actuel = 1
