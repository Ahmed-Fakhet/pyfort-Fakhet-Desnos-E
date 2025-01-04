import json
import random


def salle_De_Tresor() :
    with open('indicesSalle.json', 'r') as fichier:
        jeu_tv = json.load(fichier)
    annees = jeu_tv["Fort Boyard"].keys()
    annee = random.choice(annees)

    emissions = jeu_tv["Fort Boyard"][annee].keys()
    emission = random.choice(emissions)

    return emissions

x=salle_De_Tresor()
