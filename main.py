from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
from epreuves_mathematiques import *
from fonctions_utiles import *


def jeu():
    introduction()
    equipe = composer_equipe()
    if not equipe :
        print("Fin du jeu, il n'y a pas d'equipes ")
    print("Votre équipe est prete a gagner, que le jeu commence!!")

    cle_remportees = 0
    historique = []
    while cle_remportees < 3:
        print("menu des épreuves")
        choix_epreuve = menu_epreuves()









