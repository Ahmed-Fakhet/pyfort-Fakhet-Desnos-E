from random import
def bonneteau():
    print("Bienvenue au jeu du Bonneteau !\nTrouvez la clé en 2 essais.")
    presence_clef = randint(1, 3)
    for essai in range(2):
        try:
            x = int(input("Choisissez un bonneteau (A=1, B=2, C=3): "))
        except ValueError:
            print("Entrée non valide, réessayez.")
            continue

        if x == presence_clef:
            print("Félicitations, vous avez trouvé la clé !")
            incremente_key()
            return True
        else:
            print(f"Raté ! Il vous reste {1 - essai} essai(s).")
    return False