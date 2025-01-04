import random

def charger_enigmes():
    L_enigmes = []
    with open("Data/enigmesPF.json","r",encoding='utf-8') as fichier:
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
    enigmes = charger_enigmes()

    if not enigmes:
        print ("Il n'y a aucune enigme dispo ")
        return False
    enigme  = random.choice(enigmes)
    question = list(enigme.keys())[0]
    reponse_attendue = list(enigme.values())[0]

    print(" Le père Fouras vous demande :")
    print("-->", question)

    essais = 3
    while essais > 0 :
        reponse  = input("Veuillez indiquez votre réponse :")
        if reponse == reponse_attendue :
            print ("Bravo jeune ingénieur vous venez de remportez une clée plus qu'importante!!!")
            return True
        else :
            essais -= 1
            if essais > 0 :
                print ("Faux, il vous restes ",essais,"essai(s)")
            else :
                print ("Vous avez lamentablement echouer , la bonne reponse etait :",reponse_attendue)
                return False


enigme_pere_fouras()