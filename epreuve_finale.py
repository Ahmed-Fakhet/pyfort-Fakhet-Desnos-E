import json
import random


def salle_De_Tresor() :
    with open('Data/indicesSalle.json', 'r', encoding='utf-8') as fichier:
        jeu_tv = json.load(fichier)

    # Récupérer les années disponibles pour le jeu télévisé "Fort Boyard"
    annees = jeu_tv["Fort Boyard"].keys()
    # Choisir une année aléatoirement parmi celles disponibles
    annee = random.choice(list(annees))

    # Récupérer les émissions de l'année choisie
    emissions = jeu_tv["Fort Boyard"][annee].keys()
    # Choisir une émission aléatoirement
    emission = random.choice(list(emissions))

    # Obtenir les indices de l'émission sélectionnée
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    # Choisir un mot-code aléatoire parmi les indices
    mot_code = random.choice(indices)

    # Afficher les trois premiers indices pour aider l'utilisateur
    print("Voici les trois premiers indices : 1.",indices[0], "2.",indices[1], "3.",indices[2])
    essaies = 3
    reponse_correcte = False

    # Boucle principale pour permettre à l'utilisateur de deviner le mot-code
    while essaies > 0 :
        reponse = input("Saisir une réponse : ")
        if reponse == mot_code :
            reponse_correcte = True
            break # Quitter la boucle si la réponse est correcte
        else :
            essaies = essaies - 1 # Réduire le nombre d'essais restants
            if essaies > 0 :
                print("Il vous reste", essaies, "essaies !")
                print("Voici un autre indice",random.choice(indices[2:]))
            else :
                # Afficher le mot-code correct si l'utilisateur n'a plus d'essais
                print("le mot correcte était", mot_code ,"!")
        # Résultat final en fonction du statut de la réponse
        if reponse_correcte == True :
            print("Felicitations ! Vous avez trouvé la bonne réponse !")
        elif essaies == 0 :
            print("Hélas ! Vous n'avez pas trouvé la bonne raiponse, vous etes donc perdant.")





