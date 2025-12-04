from db_init import get_database
from models import Personnage, Monstre
import random
from utils import line, get_valid_input


def get_personnages(db):
    return [Personnage.from_dict(p) for p in db.personnage.find()]

def get_monstres(db):
    return [Monstre.from_dict(m) for m in db.monstres.find()]


def afficher_personnages(personnages):
    for i, perso in enumerate(personnages, start=1):
        print(f"{i}. {perso.nom} (ATK:{perso.ATK}, DEF:{perso.DEF}, PV:{perso.PV})")

def afficher_selection_personnages(selection):
    print("Vos personnages :")
    for perso in selection:
        print(f"- {perso.nom} (PV: {perso.PV})")

def afficher_selection_monstres(monstres):
    print("Monstres choisi :")
    for m in monstres:
        print(f"- {m.nom} (PV:{m.PV}, ATK:{m.ATK}, DEF:{m.DEF})")


        

def select_personnages(personnages):
    selection = []

    while len(selection) < 3:
        numero = get_valid_input(len(personnages))
        perso = personnages[numero - 1]

        if perso in selection:
            print("Déjà sélectionné.")
        else:
            selection.append(perso)
            print(f"{perso.nom} ajouté.")

    return selection

def select_monstres(monstres):
    return random.sample(monstres, 3)


def choix_perso(db):
    print("Choisissez 3 personnages :")
    personnages = get_personnages(db)
    afficher_personnages(personnages)
    selection = select_personnages(personnages)
    afficher_selection_personnages(selection)
    return selection

def choix_monstre(db):
    monstres = get_monstres(db)
    return random.choice(monstres)


def gestion_degats(attaquant, defenseur):
    degats = max(1, attaquant.ATK - defenseur.DEF)
    defenseur.PV -= degats
    line()
    print(f"{attaquant.nom} inflige {degats} dégâts à {defenseur.nom}. (PV restant : {defenseur.PV})")
    line()

def combat(personnages, monstre):
    print(f"fight !!! 3 perso VS {monstre.nom}")
    line()


    while True:
        for p in personnages:
            if p.PV > 0:
                gestion_degats(p, monstre)
                if monstre.PV <= 0:
                    print(f"Le monstre {monstre.nom} est vaincu !")
                    return True

        perso_vivant = [p for p in personnages if p.PV > 0]
        if len(perso_vivant) == 0:
            print("Les 3 personnages sont morts...")
            return False

        cible = random.choice(perso_vivant)
        gestion_degats(monstre, cible)


def lancer_game(db):
    print("Nouvelle partie")

    personnages = choix_perso(db)
    vague = 1

    while True:
        print(f"VAGUE {vague}")

        monstre = choix_monstre(db)
        print(f"Monstre : {monstre.nom} (PV:{monstre.PV})")

        victoire = combat(personnages, monstre)

        if victoire:
            print(f"Vague {vague} réussie !")
            vague += 1
        else:
            break

    print(f"FIN DU JEU !")
    print(f"Scores vagues : {vague - 1}")

    db.scores.insert_one({"vagues": vague - 1})

def afficher_scores(db):
    print("Scores précédents :")
    for score in db.scores.find().sort("vagues", -1).limit(3):
        print(f"- {score['vagues']} vagues")