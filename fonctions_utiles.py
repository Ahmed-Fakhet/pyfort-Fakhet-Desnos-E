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
    while n_joueurs <= 0 or n_joueurs > 3:
        n_joueurs = int(input("Veuillez entrer un nombre de joueurs égal ou inférieure à 3 . "))
    # Récupérer les informations de chaque joueur




    for i in range(n_joueurs):
        leader_valide = False
        nom = input("Saisir le nom du joueur : ")
        profession = input("Saisir le profession du joueur : ")

        leader = input("Veuillez entrer si il est leader ou pas : ")
        leader = leader.lower()

        if leader in ["oui","non"] :
            leader_valide = True
        while not leader_valide :
            leader = input("Sasie incorecte, reponder oui ou non")
            if leader in ["oui","non"] :
                leader_valide = True

        if leader == "oui" :
            est_leader = True
        else :
            est_leader = False

        dico = {"nom":nom, 'profession':profession, 'leader_valide':leader_valide, "cles_gagnees":0}
        L_joueurs.append(dico)

    return L_joueurs

composer_equipe()



def choisir_joueur(equipe): # Cette fonction sert à Selectionner un joueur
    def choisir_joueur(equipe):
        for i in range(len(equipe)):
            if equipe[i]["leader"] == "oui":
                n = "Leader"
            else:
                n = "Membre"
            print(i + 1, "{} ({}) - {}".format(equipe[i]["nom"], equipe[i]["profession"], n))
        n = int(input("Entrez le numéro du joueur choisi : "))
        while n <= 0 or n > len(equipe):
            n = int(input("Ce joueur n'éxiste pas ! Entrez à nouveau le numéro du joueur choisi : "))
        print("Vous avez choisi ", equipe[n - 1]["nom"], "comme joueur.")
        return equipe[n - 1]


def menu_epreuves(): # Menu pour choisir une épreuve parmi celles disponibles
    print("Choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif.")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du hasard")
    print("4. Énigme du Père Fouras")
    CHOIX =  input("CHOIX --> ")

    while CHOIX not in ["1","2","3","4"] :
        print("Choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif.")
        print("1. Épreuve de Mathématiques")
        print("2. Épreuve de Logique")
        print("3. Épreuve du hasard")
        print("4. Énigme du Père Fouras")
        CHOIX = input("CHOIX --> ")

    # Retourner le module correspondant à l'épreuve choisie
    if CHOIX == "1":
        return epreuves_mathematiques
    elif CHOIX == "2":
        return epreuves_logiques
    elif CHOIX == "3":
        return epreuves_hasard
    elif CHOIX == "4":
        return epreuves_logiques

