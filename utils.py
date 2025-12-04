def get_valid_input(max_choice):
    while True:
        choix = input(f"Entrez un numéro (1-{max_choice}) : ")

        if not choix.isdigit() or int(choix) < 1 or int(choix) > max_choice:
            print("Entrée invalide. Veuillez entrer un numéro entre 1 et", max_choice)
            continue
        numero = int(choix)
        if 1 <= numero <= max_choice:
            return numero


def line():
    print('-------------------------')
