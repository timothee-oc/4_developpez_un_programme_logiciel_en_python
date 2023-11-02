from controllers.menu import MenuController
from views.menu import MenuView
from utils import create_data_dirs

def main():
    menu_controller = MenuController(view=MenuView())
    menu_controller.process_choice()


if __name__ == '__main__':
    create_data_dirs()
    main()