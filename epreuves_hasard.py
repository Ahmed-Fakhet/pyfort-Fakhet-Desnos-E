import random

def bonneteau():
    bonneteau = ["A","B","C"]
    print("Bienvenue au jeu du Bonneteau !\nTrouvez la clé en 2 essais.")
    presence_clef = random.choice(1, 3)
    for essai in range(2):
        try:
            x = int(input("Choisissez un bonneteau (A=1, B=2, C=3): "))
        except ValueError:
            print("Entrée non valide, réessayez.")
            continue
        print("il vous reste ",essai,"essais")

        if x == presence_clef:
            print("Félicitations, vous avez trouvé la clé !")
            return True
        else:
            print(f"Raté ! Il vous reste {1 - essai} essai(s).")
    return False

def jeu_lance_des():
    essai = 3
    des={1,2,3,4,5,6}
    for i in range (essai) :
        print("vous avez",essai - i,"essais")
        enter=input("appuyez sur entrer pour lancez les dés !")
        des_joueur = {random.choice(des), random.choice(des)}
        des_maitre = {random.choice(des), random.choice(des)}
        print(f"Résultats du joueur : {des_joueur}")
        if 6 in des_joueur:
            print("le joueur a remporté la partie et la clé.")
            i=4
            return True
        elif 6 in des_maitre :
            print("le maitre a remporté la partie et la clé.")
            i = 4
            return False
        else :
            print("On passe au prochain tour.")
        if i == 3 and 6 not in des_maitre and 6 not in des_joueur :
            print("Match nul !")
            return False

def fonction_hasard():
    epreuves = [jeu_lance_des(), bonneteau()]
    epreuve = random.choice(epreuves)
    return epreuve

fonction_hasard()

