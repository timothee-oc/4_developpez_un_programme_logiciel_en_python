from views import MenuView
from views import PlayerView
from views import TournamentView

from controllers import MenuController
from controllers import PlayerController
from controllers import TournamentController

from utils import create_data_dirs


def main():
    """
    Entry point of the program. Instantiate all views and controllers.
    Launch the main menu.
    """
    player_view = PlayerView()
    tournament_view = TournamentView()
    menu_view = MenuView()

    player_controller = PlayerController(player_view)
    tournament_controller = TournamentController(tournament_view)
    menu_controller = MenuController(player_controller,
                                     tournament_controller,
                                     menu_view)

    menu_controller.main_menu()


if __name__ == '__main__':
    create_data_dirs()
    main()
