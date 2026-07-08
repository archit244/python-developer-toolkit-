from storage import load_expenses
from menu import main_menu


def main():
    load_expenses()
    main_menu()


main()