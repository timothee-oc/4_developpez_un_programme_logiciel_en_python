from controllers.maincontroller import MainController
from views.mainview import MainView


def main():
    main_view = MainView()
    main_controller = MainController(main_view)
    main_controller.run()


if __name__ == '__main__':
    main()
