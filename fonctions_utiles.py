# importer les autres epreuves pour avoir accés à leurs contenu
import enigme_pere_fouras
import epreuves_logiques
import epreuves_hasard
import epreuves_mathematiques
import random

def introduction(): # Introduction au jeu
    print("Le joueur doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe(): # Permet de composer une équipe de joueurs
    L_joueurs = []
    c = 0 # Compteur pour vérifier si un leader a été défini
    # Demander le nombre de joueurs, avec une limite de 3 maximum
    n_joueurs = int(input("combien de joueurs souhaitez-vous inscrire dans l'équipe ? "))
    while n_joueurs < 0 or n_joueurs > 3:
        n_joueurs = int(input("Veuillez entrer un nombre de joueurs égal ou inférieure à 3 . "))
    # Récupérer les informations de chaque joueur
    for i in range(n_joueurs):
        dico_J = {"nom":input("Saisir nom."),"profession":input("Saisir profession."),"Leader":input("Saisir si Leader ou pas (oui ou non) ."),"clées_gagnées":int(input("Saisir le nombre de clées gagnées."))}
        L_joueurs.append(dico_J)
        # Vérifier si le joueur est défini comme leader
        if dico_J["Leader"] == "oui":
            c += 1
    # Si aucun joueur n'est défini comme leader, le premier joueur devient automatiquement le leader
    if c == 0 :
        L_joueurs[0]["Leader"] = "oui"
    return L_joueurs

equipe = composer_equipe()

def choisir_joueur(equipe): # Cette fonction sert à Selectionner un joueur
    global n_joueurs
    for i in range(n_joueurs):
        SE = equipe[i]
        if SE["Leader"] == "oui":
            ROLE = "Leader"
        else:
            ROLE = "Membre"

        print(i+1,".", SE["nom"], "(", SE["profession"], ") - ", ROLE) # Affiche les joueurs et leurs information respectives

        numero = input("Entrez le numéro du joueur : ") # L'utilisateur choisit un joueur
        while numero > n_joueurs or numero < 0 :
            numero = input("Entrez un numéro valide : ")
        print(SE[numero]) # Les informations du joueurs choisit s'affiche


def menu_epreuves(): # Menu pour choisir une épreuve parmi celles disponibles
    CHOIX =  input("Choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif."
                   "1. Épreuve de Mathématiques"
                   "2. Épreuve de Logique"
                   "3. Épreuve du hasard"
                   "4. Énigme du Père Fouras"
                   "CHOIX --> ")
    liste_epreuves=["Épreuve de Mathématiques","Épreuve de Logique","Épreuve du hasard","Énigme du Père Fouras"] # Liste des choix valides
    while CHOIX not in liste_epreuves or CHOIX < "1" or CHOIX > "4" :
        CHOIX = input("Veuillez choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif."
                      "1. Épreuve de Mathématiques"
                      "2. Épreuve de Logique"
                      "3. Épreuve du hasard"
                      "4. Énigme du Père Fouras"
                      "CHOIX --> ")

    # Retourner le module correspondant à l'épreuve choisie
    if CHOIX == "1":
        return epreuves_mathematiques
    elif CHOIX == "2":
        return epreuves_logiques
    elif CHOIX == "3":
        return epreuves_hasard
    elif CHOIX == "4":
        return epreuves_logiques

