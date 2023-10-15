class MainView:
    def display_menu(self):
        print()
        print("[MENU PRINCIPAL]")
        print(" 1 Créer un tournoi")
        print(" 2 Créer un joueur")
        print(" 3 Créer un rapport")
        print(" X Quitter")
        print()

    def select_menu(self):
        choice = input("Tapez le numéro de votre choix (ou X): ")
        print()
        return choice
    
    def alert_unknown_choice(self):
        print("Entrez un numéro ou X pour quitter. Réessayez.\n")
