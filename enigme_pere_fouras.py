import random


def charger_enigmes():
    # Initialiser une liste pour stocker les énigmes
    L_enigmes = []
    # Ouvrir le fichier JSON contenant les énigmes en mode lecture
    with open("Data/enigmesPF.json","r",encoding='utf-8') as fichier:
        for ligne in fichier:
            if "question" in ligne:
                dico_enigme={} # Dictionnaire pour stocker une énigme (question : réponse)
                question = ligne[21:len(ligne)-3] # Extraire le texte de la question en supprimant les espaces ou caractères spécials
                ligne = fichier.readline()# Lire la ligne suivante pour récupérer la réponse
                reponse = ligne[20:len(ligne)-2]
                dico_enigme[question] = reponse# Ajouter la question et sa réponse au dictionnaire
                L_enigmes.append(dico_enigme)
    return L_enigmes # Retourner la liste complète des énigmes



def enigme_pere_fouras():
    enigmes = charger_enigmes() # Charger la liste des énigmes

    if not enigmes: # Vérifier si aucune énigme n'est disponible
        print ("Il n'y a aucune enigme dispo ")
        return False

    # Choisir une énigme aléatoire parmi celles disponibles
    enigme  = random.choice(enigmes)
    # Récupérer la question et la réponse attendue de l'énigme choisie
    question = list(enigme.keys())[0]
    reponse_attendue = list(enigme.values())[0]

    print(" Le père Fouras vous demande :")
    print("-->", question)

    essais = 3
    while essais > 0 : # Boucle pour permettre à l'utilisateur de répondre
        reponse  = input("Veuillez indiquez votre réponse :")  # Demander à l'utilisateur d'entrer sa réponse
        if reponse == reponse_attendue : # Vérifier si la réponse est correcte
            print ("Bravo jeune ingénieur vous venez de remportez une clée plus qu'importante!!!")
            return True # L'utilisateur a trouvé la bonne réponse
        else :
            # Réduire le nombre d'essais restants
            essais -= 1
            if essais > 0 :
                # Informer l'utilisateur du nombre d'essais restants
                print ("Faux, il vous reste ",essais,"essai(s)")
            else : # Afficher la bonne réponse si l'utilisateur échoue
                print ("Vous avez lamentablement echouer , la bonne reponse etait :",reponse_attendue)
                return False # L'utilisateur a échoué


