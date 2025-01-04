import enigme_pere_fouras
import epreuves_logiques
import epreuves_hasard
import epreuves_mathematiques

def introduction():
    print("Le joueur doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe():
    L_joueurs = []
    c = 0
    n_joueurs = int(input("combien de joueurs souhaitez-vous inscrire dans l'équipe ? "))
    while n_joueurs < 0 or n_joueurs > 3:
        n_joueurs = int(input("Veuillez entrer un nombre de joueurs égal ou inférieure à 3 . "))
    for i in range(n_joueurs):
        dico_J = {"nom":input("Saisir nom."),"profession":input("Saisir profession."),"Leader":input("Saisir si Leader ou pas (oui ou non) ."),"clées_gagnées":int(input("Saisir le nombre de clées gagnées."))}
        L_joueurs.append(dico_J)
        if dico_J["Leader"] == "oui":
            c += 1
    if c == 0 :
        L_joueurs[0]["Leader"] = "oui"
    return L_joueurs

def menu_epreuves():
    CHOIX =  input("Choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif."
                   "1. Épreuve de Mathématiques"
                   "2. Épreuve de Logique"
                   "3. Épreuve du hasard"
                   "4. Énigme du Père Fouras"
                   "CHOIX --> ")
    liste_epreuves=["Épreuve de Mathématiques","Épreuve de Logique","Épreuve du hasard","Énigme du Père Fouras"]
    while CHOIX not in liste_epreuves or CHOIX < "1" or CHOIX > "4" :
        CHOIX = input("Veuillez choisir parmis les epreuves disponibles en selectionnant leur chiffre respectif."
                      "1. Épreuve de Mathématiques"
                      "2. Épreuve de Logique"
                      "3. Épreuve du hasard"
                      "4. Énigme du Père Fouras"
                      "CHOIX --> ")

    if CHOIX == "1":
        return epreuves_mathematiques
    elif CHOIX == "2":
        return epreuves_logiques
    elif CHOIX == "3":
        return epreuves_hasard
    elif CHOIX == "4":
        return epreuves_logiques

