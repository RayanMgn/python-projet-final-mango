from db_init import get_database
import random

def get_personnages(db):
    """Retourne tous les personnages depuis MongoDB"""
    return list(db.personnage.find())

def get_monstres(db):
    """Retourne tous les monstres depuis MongoDB"""
    return list(db.monstres.find())

def afficher_personnages(personnages):
    """Affiche la liste des personnages avec des numéros"""
    for i, perso in enumerate(personnages, start=1):
        print(f"{i}. {perso['nom']}")

def afficher_selection_personnages(selection):
    print("=== Vos personnages sélectionnés ===")
    for perso in selection:
        print(f"- {perso['nom']}")

def afficher_selection_monstres(selection):
    print("=== Monstres sélectionnés ===")
    for m in selection:
        print(f"- {m['nom']}")

def verif_input(user_input, max_choice):
    """Vérifie que l'entrée utilisateur est un numéro correct"""
    try:
        num = int(user_input)
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return None

    if not (1 <= num <= max_choice):
        print("Veuillez entrer un numéro valide.")
        return None

    return num

def select_personnages(personnages):
    """Permet à l'utilisateur de sélectionner 3 personnages"""

    selection = []

    while len(selection) < 3:
        choix = input(f"Sélection {len(selection)+1}/3 → Entrez un numéro : ")

        numero = verif_input(choix, len(personnages))
        if numero is None:
            continue

        perso = personnages[numero - 1]

        if perso in selection:
            print("Ce personnage est déjà sélectionné.")
        else:
            selection.append(perso)
            print(f"Ajouté : {perso['nom']}")

    return selection


def select_monstres(monstres):
    """Sélectionne 3 monstres aléatoirement (ou moins si base vide)"""
    count = len(monstres)

    return random.sample(monstres, 3)


def choix_perso(db):
    print("Lancement d'une nouvelle game...")
    print("Choisissez 3 personnages parmi cette liste :")

    personnages = get_personnages(db)

    afficher_personnages(personnages)

    selection = select_personnages(personnages)
    afficher_selection_personnages(selection)

    return selection


def choix_monstre(db):
    print("Sélection aléatoire de 3 monstres...")

    monstres = get_monstres(db)

    selection = select_monstres(monstres)
    afficher_selection_monstres(selection)

    return selection


def lancer_game(db):
    print("Lancement d'une nouvelle game...")

    personnages = choix_perso(db)
    monstres = choix_monstre(db)


    print("Début de la Partie !!")

