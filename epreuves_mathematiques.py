import random # Importer le module random pour générer des valeurs aléatoires
a = random.randint(1,10)
b = random.randint(1,10)
def resoudre_equation_lineaire(a,b): # Fonction pour résoudre une équation linéaire de la forme ax + b = 0
    x = -b/a # Calcul de la solution
    return a,b,x

S=False

# Fonction représentant une épreuve mathématique pour résoudre une équation
def epreuve_math_equation():
    global a,b,S
    a, b, x = resoudre_equation_lineaire(a,b)
    print("Resoudre : ",a,"x +", b, "=", 0) # Afficher l'équation
    X=float(input("Saisir la solution X :")) # Demander la solution au joueur
    if x == X: # Vérifier si la réponse est correcte
        S=True
    return S


n = random.randint(1, 10) # Génère un nombre aléatoire entre 1 et 10


import random
# Fonction pour calculer la factorielle d'un nombre
def factorielle(n) :
    res=1
    for i in range(1,n+1):
        res *= i
    print(res) # Afficher la factorielle
    return res



def epreuve_factorielle(): # Epreuve demandant au joueur de calculer une factorielle
    m = int(input("Quelle est la factoriolle de ",n," ?")) # Demander la réponse au joueur
    factorielle(n)
    if m == n: # Vérifier si la réponse est correcte
        print ("Vous avez gagnée une clée")
        return True
    else:
        print("Vous n'avez pas gagner de clée vous etes un looser")
        return False


# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

# Fonction pour trouver le premier nombre supérieur à n qui est premier
def premier_plus_proche(n):
    while not est_premier(n): # Répéter jusqu'à ce qu'un nombre premier soit trouvé
        n += 1
    return n


# Epreuve demandant de trouver le plus proche nombre premier supérieur
def epreuve_math_premier(n):
    n = random.randint(10,20) # Génère un entier aléatoire entre 10 et 20
    reponse = int(input("veuillez saisir l'entier supérieur premier le plus proche de n"))
    premier_plus_proche(n)
    if n == reponse: # Vérifier si la réponse est correcte
        print("Bravo vous etes le meilleur vous venez de remporter une clef")
        return True
    else:
        print("Il s'agirait de faire des efforts vous etes en école d'ingénieur. Vous venez de perdre une clée")
        return False


# Epreuve demandant des calculs sur une liste de nombres
def epreuve_roulette_mathematiques():
    nombres = [random.randint(1, 20) for _ in range(5)] # Génère une liste de 5 nombres aléatoires
    print(nombres)
    operation = random.choice(['addition', 'soustraction', 'multiplication']) # Choisir une opération aléatoire
    somme = 0
    sommeprod = 1
    # Calculer le résultat de l'opération choisie
    for i in range(len(nombres)):
        if operation == 'addition':
            somme += nombres[i]
        elif operation == 'soustraction':
            somme -= nombres[i]
        else :
            sommeprod *= nombres[i]
    # Demander la réponse au joueur
    reponse = int(input("quelle est le resultat de l'/la", operation, "entre les nombres de la liste : nombres ??"))
    if operation == 'addition' or 'soustraction':
        if reponse == somme :
            print("Bravo ingénieur de demain vous venez de remportez une clef , vous etes sur le chemin de la réussite et de la victoire!!!!!!")
            return True
        else :
            print ("Vous ne faites aucun effort , il s'agirait de se ressaisir !!!!")
            return False
    else :
        if reponse == sommeprod :
            print("Bravo ingénieur de demain vous venez de remportez une clef , vous etes sur le chemin de la réussite et de la victoire!!!!!!")
            return True
        else :
            print("Vous ne faites aucun effort , il s'agirait de se ressaisir !!!!")
            return False


# Fonction principale pour sélectionner et exécuter une épreuve mathématique
def epreuve_math():
    epreuves = [
        epreuve_factorielle,
        epreuve_math_equation,
        epreuve_math_premier,
        epreuve_roulette_mathematiques
    ]
    # Sélectionner une épreuve de manière aléatoire
    epreuve = random.choice(epreuves)
    return epreuve # Exécuter l'épreuve sélectionnée et retourner son résultat



