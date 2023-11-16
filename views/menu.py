class MenuView():
    def choice_main(self):
        choice = input(
            "[MENU PRINCIPAL]\n"
            " 1. Gestion des tournois\n"
            " 2. Créer un joueur\n"
            " 3. Générer des rapports\n"
            " Laissez vide pour quitter\n"
            " => "
        )
        print()
        return choice

    def choice_tournament(self):
        choice = input(
            "[MENU TOURNOI]\n"
            " 1. Créer un tournoi\n"
            " 2. Inscrire des joueurs à un tournoi\n"
            " 3. (Re)Lancer un tournoi\n"
            " Laissez vide pour revenir au menu principal\n"
            " => "
        )
        print()
        return choice

    def choice_report(self):
        choice = input(
            "[MENU RAPPORT]\n"
            " 1. Liste de tous les joueurs\n"
            " 2. Liste de tous les tournois\n"
            " 3. Chercher un tournoi\n"
            " 4. Liste des joueurs d'un tournoi\n"
            " 5. Liste des tours d'un tournoi\n"
            " Laissez vide pour revenir au menu principal\n"
            " => "
        )
        print()
        return choice

    def alert_unknown_choice(self, choice):
        print(f"Erreur: {choice} ne correspond à aucune option !\n")
