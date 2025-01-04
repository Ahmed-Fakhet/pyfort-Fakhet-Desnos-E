from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
from epreuves_mathematiques import *
from fonctions_utiles import *
import random


def jeu():


    introduction()
    equipe = composer_equipe()
    if not equipe:
        print("Aucune équipe n'a été créée. Fin du jeu.")
        return

    print("L'équipe est prête ! Que le jeu commence.")


    cles_gagnees = 0


    historique = []

    while cles_gagnees < 3:
        print(" Menu des épreuves ")
        choix_epreuve = menu_epreuves()


        print("Sélection du joueur ")
        joueur = random.randint(equipe)
        if not joueur:
            print("Aucun joueur sélectionné. Fin de la partie.")
            return

        print(f"\n{joueur['nom']} va participer à l'épreuve !")


        epreuve_reussie = False
        if choix_epreuve == 1:
            epreuve_reussie = epreuve_math()
        elif choix_epreuve == 2:
            epreuve_reussie = jeu_nim()
        elif choix_epreuve == 3:
            epreuve_reussie = fonction_hasard()
        elif choix_epreuve == 4:
            epreuve_reussie = enigme_pere_fouras()

        if epreuve_reussie:
            print(joueur['nom'],"a réussi l'épreuve et gagne une clé !")
            joueur['cles_gagnees'] += 1
            cles_gagnees += 1
        else:
            print(joueur['nom'], "a échoué à l'épreuve.")
        historique.append({
            "epreuve": choix_epreuve,
            "joueur": joueur["nom"],
            "reussite": epreuve_reussie
        })


    print(" Épreuve finale : La salle du trésor")
    victoire = salle_De_Tresor()

    if victoire:
        print("Félicitations ! Vous avez ouvert la salle du trésor et gagné le jeu ! ")
    else:
        print("Dommage ! Vous n'avez pas réussi à ouvrir la salle du trésor. Fin du jeu.")

if __name__ == "__main__":
    jeu()











