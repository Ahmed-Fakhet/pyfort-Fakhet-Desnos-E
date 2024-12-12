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

def jeu_lance_des():
    essai = 3
    des={1,2,3,4,5,6}
    for i in range (3) :
        print("vous avez",essai - i,"essais")
        enter=input("appuyez sur entrer pour lancez les dés !")
        des_joueur = {random.choice(des), random.choice(des)}
        des_maitre = {random.choice(des), random.choice(des)}
        print(f"Résultats du joueur : {des_joueur}")
        if 6 in des_joueur:
            print("Félicitations ! Vous avez obtenu un 6 et gagné la partie et donc la clé.")
            return True
            break




