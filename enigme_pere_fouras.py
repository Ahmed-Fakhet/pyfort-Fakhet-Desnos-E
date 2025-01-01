import random

def charger_enigmes(fichier):
    L_enigmes= []
    with open("enigmesPF.json","r") as fichier:
        for ligne in fichier:
            if "question" in ligne:
                dico_enigme={}
                question = ligne[21:len(ligne)-3]
                ligne = fichier.readline()
                reponse = ligne[20:len(ligne)-2]
                dico_enigme[question] = reponse
                L_enigmes.append(dico_enigme)
    return L_enigmes



def enigme_pere_fouras():
    global L_enigmes
    enigme=random.choice(L_enigmes)
    print(enigme[ke])