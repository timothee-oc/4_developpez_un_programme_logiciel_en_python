class MenuView:
    def choice_main(self):
        choice = input(
            "\n[MENU PRINCIPAL]\n"
            " 1. Gestion des tournois\n"
            " 2. Gestion des joueurs\n"
            " 3. Gestion des rapports\n"
            " 4. Quitter\n"
            " => "
        )
        print()
        return choice
    
    def choice_tournament(self):
        choice = input(
            "\n[MENU TOURNOI]\n"
            " 1. Créer un tournoi\n"
            " 2. (Re)Lancer un tournoi\n"
            " 3. Retour\n"
            " => "
        )
        print()
        return choice
    
    def choice_player(self):
        choice = input(
            "\n[MENU JOUEUR]\n"
            " 1. Créer un joueur\n"
            " 2. Chercher un joueur\n"
            " 3. Retour\n"
            " => "
        )
        print()
        return choice
    
    def choice_report(self):
        choice = input(
            "\n[MENU RAPPORT]\n"
            " 1. Liste de tous les joueurs\n"
            " 2. Liste de tous les tournois\n"
            " 3. Chercher un tournoi\n"
            " 4. Liste des joueurs d'un tournoi\n"
            " 5. Liste des tours d'un tournoi\n"
            " 6. Retour\n"
            " => "
        )
        print()
        return choice
    
    def alert_unknown_choice(self, choice):
        print(f"Erreur: {choice} ne correspond à aucune option !\n")