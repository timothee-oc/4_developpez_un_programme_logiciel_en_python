from views import MainView
from views import MatchView
from views import PlayerView
from views import RoundView
from views import TournamentView

from controllers import MainController
from controllers import MatchController
from controllers import PlayerController
from controllers import RoundController
from controllers import TournamentController

from utils import create_data_dirs


def main():
    match_view = MatchView()
    player_view = PlayerView()
    round_view = RoundView()
    tournament_view = TournamentView()
    main_view = MainView()

    match_controller = MatchController(match_view)
    player_controller = PlayerController(player_view)
    round_controller = RoundController(round_view)
    tournament_controller = TournamentController(tournament_view)
    main_controller = MainController(match_controller, player_controller,
                                     round_controller, tournament_controller,
                                     main_view)

    main_controller.main_menu()


if __name__ == '__main__':
    create_data_dirs()
    main()
