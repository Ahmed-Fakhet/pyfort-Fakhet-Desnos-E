import json
import random


def salle_De_Tresor() :
    with open('Data/indicesSalle.json', 'r', encoding='utf-8') as fichier:
        jeu_tv = json.load(fichier)
    annees = jeu_tv["Fort Boyard"].keys()
    annee = random.choice(list(annees))

    emissions = jeu_tv["Fort Boyard"][annee].keys()
    emission = random.choice(list(emissions))

    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = random.choice(indices)

    print("Voici les trois premiers indices : 1.",indices[0], "2.",indices[1], "3.",indices[2])
    essaies = 3
    reponse_correcte = False

    while essaies > 0 :
        reponse = input("Saisir une réponse :")
        if reponse == mot_code :
            reponse_correcte = True
            break
        else :
            essaies = essaies - 1
            if essaies > 0 :
                print("Il vous reste", essaies, "essaies !")
                print("Voici un autre indice",random.choice(indices[2:]))
            else :
                print("le mote correcte était", mot_code ,"!")
            if reponse_correcte == True :
                print("Felicitations ! Vous avez trouvé la bonne réponse !")
            elif essaies == 0 :
                print("Hélas ! Vous n'avez pas trouvé la bonne raiponse, vous etes donc perdant.")





