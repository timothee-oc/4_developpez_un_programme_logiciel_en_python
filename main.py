from views.main_view import MainView
from views.match import MatchView
from views.player import PlayerView
from views.report import ReportView
from views.round import RoundView
from views.tournament import TournamentView

from controllers.main_controller import MainController
from controllers.match import MatchController
from controllers.player import PlayerController
from controllers.report import ReportController
from controllers.round import RoundController
from controllers.tournament import TournamentController

from utils import create_data_dirs

def main():
    match_view = MatchView()
    player_view = PlayerView()
    report_view = ReportView()
    round_view = RoundView()
    tournament_view = TournamentView()
    main_view = MainView()

    match_controller = MatchController(match_view)
    player_controller = PlayerController(player_view)
    report_controller = ReportController(report_view)
    round_controller = RoundController(round_view)
    tournament_controller = TournamentController(tournament_view)
    main_controller = MainController(match_controller, player_controller,
                                     report_controller, round_controller, tournament_controller,
                                     main_view)

    main_controller.main_menu()


if __name__ == '__main__':
    create_data_dirs()
    main()