# Importation des modules nécessaires
# Chaque module contient des fonctions ou des classes pour gérer les différentes parties du jeu.
from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
from epreuves_mathematiques import *
from fonctions_utiles import *
import random  # Utilisé pour sélectionner un joueur aléatoire

# Définition de la fonction principale du jeu
def jeu():
    # Introduction au jeu
    introduction()

    # Création de l'équipe de joueurs
    equipe = composer_equipe()

    print("L'équipe est prête ! Que le jeu commence.")


    # Initialisation des variables
    cles_gagnees = 0  # Compte le nombre total de clés gagnées

    # Boucle principale du jeu : s'exécute jusqu'à ce que 3 clés soient gagnées
    while cles_gagnees < 3:

        joueur = choisir_joueur(equipe)

        # Affiche le menu des épreuves et permet au joueur de choisir une épreuve
        print(" Menu des épreuves ")
        choix_epreuve = menu_epreuves()

        # Initialisation du statut de réussite de l'épreuve
        epreuve_reussie = False

        # Gestion des épreuves en fonction du choix de l'utilisateur
        if choix_epreuve == 1:
            epreuve_reussie = epreuve_math()  # Épreuve mathématique
        elif choix_epreuve == 2:
            epreuve_reussie = jeu_nim()  # Épreuve logique : jeu de Nim
        elif choix_epreuve == 3:
            epreuve_reussie = fonction_hasard()  # Épreuve basée sur le hasard
        elif choix_epreuve == 4:
            enigme_pere_fouras.enigme_pere_fouras()  # Enigme posée par le Père Fouras

        # Gestion du résultat de l'épreuve
        if epreuve_reussie:
            print(joueur['nom'], "a réussi l'épreuve et gagne une clé !")
            joueur['cles_gagnées'] += 1  # Mise à jour du nombre de clés du joueur
            cles_gagnees += 1  # Mise à jour du nombre total de clés gagnées
        else:
            print(joueur['nom'], "a échoué à l'épreuve.")


    # Lorsque 3 clés sont gagnées, on passe à l'épreuve finale
    print(" Épreuve finale : La salle du trésor")
    victoire = salle_De_Tresor()  # Appel de la fonction gérant l'épreuve finale

    # Gestion de la victoire ou de la défaite dans l'épreuve finale
    if victoire:
        print("Félicitations ! Vous avez ouvert la salle du trésor et gagné le jeu !")
    else:
        print("Dommage ! Vous n'avez pas réussi à ouvrir la salle du trésor. Fin du jeu.")

# Vérifie si le script est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    jeu()  # Appelle la fonction principale pour démarrer le jeu













