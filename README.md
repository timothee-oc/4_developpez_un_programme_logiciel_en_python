# Instructions

* Installez Python (version >= 3.11.5), et assurez vous que pip est bien installé avec (version >= 23.2.1)
* Clonez ce repo dans un répertoire local
* Créez un environnement virtuel avec la commande : `py -m venv venv`
* Entrez dans votre environnement virtuel avec la commande : `.\env\Scripts\activate`
* Installez les librairies du fichier **requirements.txt** dans votre environnement virtuel avec la commande `pip install -r requirements.txt`
* Exécutez le programme **main.py** avec la commande `py main.py`
* Pour générer un rapport flake8, utilisez la commande `flake8`
* Le rapport peut être consulté en ouvrant le fichier **flake-report/index.html** dans votre navigateur

# Utilisation du programme

Ce programme permet de gérer des tournois d'échecs et repose sur une base de données de fichiers JSON qui permet de sauver les données des tournois et des joueurs.
Cette base de données se trouve dans le répertoire **data** qui sera créé par le programme.
Le programme permet de créer de nouveaux tournois ou joueurs, d'inscrire des joueurs à des tournois et de joueur ces tournois.
Vous pouvez couper le programme entre deux matchs d'un tournoi et reprendre où vous vous en étiez arrêté.
Le programme permet également de générer des rapports tels que la liste des joueurs en base de données ou les résultats des rounds d'un tournoi.