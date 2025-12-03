from db_init import get_database
import sys
from game import lancer_game

def afficher_scores():
    print("Affichage des scores...")

def main():
    db = get_database() 

    while True:
        print("=== Menu ToDo ===")
        print("1. Lancer une game")
        print("2. Afficher les scores")
        print("3. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            lancer_game(db)

        elif choice == "2":
            afficher_scores(db)

        elif choice == "3":
            print("Fermeture de l’application. À bientôt !")
            sys.exit(0)

        else:
            print("Choix invalide. Veuillez réessayer.\n")

if __name__ == "__main__":
    main()
