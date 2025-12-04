def get_valid_input(max_choice):
    while True:
        choix = input(f"Entrez un numéro (1-{max_choice}) : ")
        numero = int(choix)
        if 1 <= numero <= max_choice:
            return numero


def line():
    print('-------------------------')
