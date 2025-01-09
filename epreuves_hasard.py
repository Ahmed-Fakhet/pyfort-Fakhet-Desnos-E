import random # Importation du module random

def bonneteau():
    # Attribuer les positions des bonneteaux
    bonneteau = ["A","B","C"]
    print("Bienvenue au jeu du Bonneteau !\nTrouvez la clé en 2 essais.")
    # Choix aléatoire de la position de la clé (1, 2 ou 3 équivalan à A, B, C)
    presence_clef = random.randint(1, 3)
    # L'utilisateur a 2 essais pour trouver la clé
    essai = 2
    print("Vous avez", essai, "essaies .")
    for i in range(2):
        # Demande au joueur de choisir un bonneteau (entre A, B, C)
        x = int(input("Choisissez un bonneteau (A=1, B=2, C=3): "))
        while x < 1 or x > 3:
            x = int(input("Entrée non valide, réessayez."))
        # Vérifie si le joueur a trouvé la clé
        essai -= 1
        if x == presence_clef:
            print("Félicitations, vous avez trouvé la clé !")
            return True # Le joueur gagne donc on retourne True
        elif essai == 0:
            print("Vous avez perdu !")
            return False
        else:
            print(f"Raté ! Il vous reste {essai} essai(s).")
            # Si aucun essai n'a permis de trouver la clé, le joueur perd.




def jeu_lance_des():
    essai = 3
    des={1,2,3,4,5,6}
    # Boucle pour effectuer les essais
    for i in range (essai) :
        print("vous avez",essai - i,"essais")
        enter=input("appuyez sur entrer pour lancez les dés !")
        # Générer deux dés pour le joueur et deux dés pour le maître
        des_joueur = (random.randint(1,6), random.randint(1,6))
        des_maitre = (random.randint(1,6), random.randint(1,6))
        print(f"Résultats du joueur : {des_joueur}")
        print(f"Résultats du maitre : {des_maitre}")
        # Vérifier si le joueur a obtenu un 6
        if 6 in des_joueur:
            print("le joueur a remporté la partie et la clé.")
            i=4
            return True
        # Vérifier si le maître a obtenu un 6
        elif 6 in des_maitre :
            print("le maitre a remporté la partie et la clé. Vous avez donc perdu !")
            i = 4
            return False
        # Si aucun 6 n'est obtenu, on passe au prochain tour
        else :
            print("Pas de 6 dans les deux camps, on passe au prochain tour.")
        # Si c'est le dernier essai et qu'aucun 6 n'est obtenu, déclarer un match nul
        if i == 3 and 6 not in des_maitre and 6 not in des_joueur :
            print("Match nul !")
            return False

def fonction_hasard():
    # Liste des épreuves disponibles
    epreuves = [jeu_lance_des, bonneteau] # Assurez-vous que `bonneteau()` est défini ailleurs
    epreuve = random.choice(epreuves) # Choisir une épreuve aléatoire
    return epreuve() # Retourner le résultat de l'épreuve sélectionnée



