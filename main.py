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
    # Introduction au jeu (probablement une fonction qui affiche une introduction au joueur)
    introduction()

    # Création de l'équipe de joueurs
    equipe = composer_equipe()
    if not equipe:  # Vérification si l'équipe est vide
        print("Aucune équipe n'a été créée. Fin du jeu.")
        return  # Arrêt du programme si aucune équipe n'est créée

    print("L'équipe est prête ! Que le jeu commence.")

    # Initialisation des variables
    cles_gagnees = 0  # Compte le nombre total de clés gagnées
    historique = []  # Liste pour suivre les épreuves jouées et leurs résultats

    # Boucle principale du jeu : s'exécute jusqu'à ce que 3 clés soient gagnées
    while cles_gagnees < 3:
        print(" Menu des épreuves ")

        # Affiche le menu des épreuves et permet au joueur de choisir une épreuve
        choix_epreuve = menu_epreuves()

        # Sélection aléatoire d'un joueur de l'équipe
        print("Sélection du joueur ")
        joueur = random.randint(equipe)  # Erreur ici : `random.randint` doit être remplacé par `random.choice`
        if not joueur:  # Vérifie si un joueur a bien été sélectionné
            print("Aucun joueur sélectionné. Fin de la partie.")
            return

        print(f"\n{joueur['nom']} va participer à l'épreuve !")

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
            epreuve_reussie = enigme_pere_fouras()  # Enigme posée par le Père Fouras

        # Gestion du résultat de l'épreuve
        if epreuve_reussie:
            print(joueur['nom'], "a réussi l'épreuve et gagne une clé !")
            joueur['cles_gagnees'] += 1  # Mise à jour du nombre de clés du joueur
            cles_gagnees += 1  # Mise à jour du nombre total de clés gagnées
        else:
            print(joueur['nom'], "a échoué à l'épreuve.")

        # Enregistrement des résultats de l'épreuve dans l'historique
        historique.append({
            "epreuve": choix_epreuve,  # Numéro de l'épreuve jouée
            "joueur": joueur["nom"],  # Nom du joueur ayant participé
            "reussite": epreuve_reussie  # Résultat de l'épreuve (True ou False)
        })

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












