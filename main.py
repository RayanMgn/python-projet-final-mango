from db_init import get_database
import sys
from game import lancer_game
from game import afficher_scores
from utils import line
from utils import get_valid_input

def print_menu():
    print(" Menu Principal ")
    line()    
    print("1. Lancer une game")
    line()
    print("2. Afficher les scores")
    line()
    print("3. Quitter")
    line()

def main():
    db = get_database() 

    while True:
        
        print_menu()

        choix = get_valid_input(3)

        if choix == 1:
            lancer_game(db)

        elif choix == 2:
            afficher_scores(db)

        elif choix == 3:
            print("Fermeture de l’application. À bientôt !")
            sys.exit(0)

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
