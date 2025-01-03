import random # Importation du module random

def bonneteau():
    # Attribuer les positions des bonneteaux
    bonneteau = ["A","B","C"]
    print("Bienvenue au jeu du Bonneteau !\nTrouvez la clé en 2 essais.")
    # Choix aléatoire de la position de la clé (1, 2 ou 3 équivalan à A, B, C)
    presence_clef = random.choice(1, 3)
    # L'utilisateur a 2 essais pour trouver la clé
    for essai in range(2):
        try:
            # Demande au joueur de choisir un bonneteau (entre A, B, C)
            x = int(input("Choisissez un bonneteau (A=1, B=2, C=3): "))
        except ValueError:
            print("Entrée non valide, réessayez.")
            continue # Passe à l'itération suivante
        print("il vous reste ",essai,"essais")
        # Vérifie si le joueur a trouvé la clé
        if x == presence_clef:
            print("Félicitations, vous avez trouvé la clé !")
            return True # Le joueur gagne donc on retourne True
        else:
            print(f"Raté ! Il vous reste {1 - essai} essai(s).")
            # Si aucun essai n'a permis de trouver la clé, le joueur perd.
    return False

def jeu_lance_des():
    essai = 3
    des={1,2,3,4,5,6}
    # Boucle pour effectuer les essais
    for i in range (essai) :
        print("vous avez",essai - i,"essais")
        enter=input("appuyez sur entrer pour lancez les dés !")
        # Générer deux dés pour le joueur et deux dés pour le maître
        des_joueur = {random.choice(des), random.choice(des)}
        des_maitre = {random.choice(des), random.choice(des)}
        print(f"Résultats du joueur : {des_joueur}")
        # Vérifier si le joueur a obtenu un 6
        if 6 in des_joueur:
            print("le joueur a remporté la partie et la clé.")
            i=4
            return True
        # Vérifier si le maître a obtenu un 6
        elif 6 in des_maitre :
            print("le maitre a remporté la partie et la clé.")
            i = 4
            return False
        # Si aucun 6 n'est obtenu, on passe au prochain tour
        else :
            print("On passe au prochain tour.")
        # Si c'est le dernier essai et qu'aucun 6 n'est obtenu, déclarer un match nul
        if i == 3 and 6 not in des_maitre and 6 not in des_joueur :
            print("Match nul !")
            return False

def fonction_hasard():
    # Liste des épreuves disponibles
    epreuves = [jeu_lance_des(), bonneteau()] # Assurez-vous que `bonneteau()` est défini ailleurs
    epreuve = random.choice(epreuves) # Choisir une épreuve aléatoire
    return epreuve # Retourner le résultat de l'épreuve sélectionnée



