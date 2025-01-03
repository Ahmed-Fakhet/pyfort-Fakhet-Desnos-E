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
S = epreuve_math_equation()
print(S)



import random
def factorielle(n) :
    res=1
    for i in range(1,n+1):
        res *= i
    print(res)
    return res

def epreuve_factorielle():
    n = random.randint(1, 10)
    print(n)
    m = int(input("Quelle est la factoriolle de n ??"))
    factorielle(n)
    if m == n:
        print ("Vous avez gagnée une clée")
        return True
    else:
        print("Vous n'avez pas gagner de clée vous etes un looser")
        return False



def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n

def epreuve_math_premier(n):
    n = random.randint(10,20)
    reponse = int(input("veuillez saisir l'entier supérieur premier le plus proche de n"))
    premier_plus_proche(n)
    if n == reponse:
        print("Bravo vous etes le meilleur vous venez de remporter une clef")
        return True
    else:
        print("Il s'agirait de faire des efforts vous etes en école d'ingénieur. Vous venez de perdre une clée")
        return False



def epreuve_roulette_mathematiques():
    nombres = [random.randint(1, 20) for _ in range(5)]
    print(nombres)
    operation = random.choice(['addition', 'soustraction', 'multiplication'])
    somme = 0
    sommeprod = 1
    for i in range(len(nombres)):
        if operation == 'addition':
            somme += nombres[i]
        elif operation == 'soustraction':
            somme -= nombres[i]
        else :
            sommeprod *= nombres[i]
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



def epreuve_math():
    epreuves = [
        epreuve_factorielle,
        epreuve_math_equation,
        epreuve_math_premier,
        epreuve_roulette_mathematiques
    ]
    epreuve = random.choice(epreuves)
    return epreuve()



