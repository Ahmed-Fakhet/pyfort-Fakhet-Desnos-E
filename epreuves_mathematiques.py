import random

# Génère deux nombres aléatoires a et b
a = random.randint(1, 10)
b = random.randint(1, 10)

# Fonction pour résoudre une équation linéaire de la forme ax + b = 0
def resoudre_equation_lineaire(a, b):
    x = -b / a  # Calcul de la solution x
    return a, b, x  # Retourne les coefficients et la solution

S = False  # Variable pour suivre le succès de l'épreuve

# Fonction pour effectuer l'épreuve sur une équation linéaire
def epreuve_math_equation():
    global a, b, S  # Accès aux variables globales
    a, b, x = resoudre_equation_lineaire(a, b)  # Résolution de l'équation
    print("Resoudre : ", a, "x +", b, "=", 0)  # Affiche l'équation à résoudre
    X = float(input("Saisir la solution X :"))  # Demande la solution à l'utilisateur
    if x == X:  # Vérifie si la réponse est correcte
        S = True
    return S  # Retourne le résultat de l'épreuve

# Appelle la fonction d'épreuve et affiche le résultat
S = epreuve_math_equation()
print(S)  # Affiche si l'utilisateur a réussi ou non

# Fonction pour calculer la factorielle d'un nombre
def factorielle(n):
    res = 1  # Initialisation de la variable résultat
    for i in range(1, n + 1):  # Boucle pour multiplier tous les entiers de 1 à n
        res *= i
    print(res)  # Affiche la factorielle
    return res  # Retourne la factorielle

# Fonction pour une épreuve basée sur le calcul de factorielle
def epreuve_factorielle():
    n = random.randint(1, 10)  # Génère un entier aléatoire
    print(n)  # Affiche l'entier
    m = int(input("Quelle est la factoriolle de n ??"))  # Demande la réponse à l'utilisateur
    factorielle(n)  # Calcule la factorielle
    if m == n:  # Compare la réponse utilisateur au nombre généré (erreur logique ici)
        print("Vous avez gagnée une clée")  # Message de succès
        return True
    else:
        print("Vous n'avez pas gagner de clée vous etes un looser")  # Message d'échec
        return False

# Vérifie si un nombre est premier
def est_premier(n):
    if n <= 1:  # Les nombres <= 1 ne sont pas premiers
        return False
    for i in range(2, n):  # Vérifie les diviseurs potentiels
        if n % i == 0:  # Si divisible, n n'est pas premier
            return False
    return True  # Si aucun diviseur, n est premier

# Trouve le nombre premier supérieur ou égal à n
def premier_plus_proche(n):
    while not est_premier(n):  # Tant que n n'est pas premier
        n += 1  # Incrémente n pour trouver le suivant
    return n

# Épreuve mathématique pour trouver un nombre premier
def epreuve_math_premier(n):
    n = random.randint(10, 20)  # Génère un nombre aléatoire entre 10 et 20
    reponse = int(input("veuillez saisir l'entier supérieur premier le plus proche de n"))  # Demande une réponse
    premier_plus_proche(n)  # Calcule le premier plus proche
    if n == reponse:  # Vérifie la réponse utilisateur (erreur logique ici)
        print("Bravo vous etes le meilleur vous venez de remporter une clef")  # Message de succès
        return True
    else:
        print("Il s'agirait de faire des efforts vous etes en école d'ingénieur. Vous venez de perdre une clée")  # Message d'échec
        return False

# Épreuve mathématique avec des opérations aléatoires
def epreuve_roulette_mathematiques():
    nombres = [random.randint(1, 20) for _ in range(5)]  # Génère une liste de 5 nombres aléatoires
    print(nombres)  # Affiche la liste
    operation = random.choice(['addition', 'soustraction', 'multiplication'])  # Choisit une opération au hasard
    somme = 0  # Initialisation de la somme pour addition ou soustraction
    sommeprod = 1  # Initialisation du produit pour multiplication
    for i in range(len(nombres)):  # Parcourt la liste des nombres
        if operation == 'addition':  # Si addition, ajoute les nombres
            somme += nombres[i]
        elif operation == 'soustraction':  # Si soustraction, soustrait les nombres
            somme -= nombres[i]
        else:  # Sinon, multiplie les nombres
            sommeprod *= nombres[i]
    reponse = int(input("quelle est le resultat de l'/la", operation, "entre les nombres de la liste : nombres ??"))  # Demande le résultat
    if operation == 'addition' or 'soustraction':  # Vérifie le résultat pour addition ou soustraction
        if reponse == somme:
            print("Bravo ingénieur de demain vous venez de remportez une clef , vous etes sur le chemin de la réussite et de la victoire!!!!!!")
            return True
        else:
            print("Vous ne faites aucun effort , il s'agirait de se ressaisir !!!!")
            return False
    else:  # Vérifie le résultat pour multiplication
        if reponse == sommeprod:
            print("Bravo ingénieur de demain vous venez de remportez une clef , vous etes sur le chemin de la réussite et de la victoire!!!!!!")
            return True
        else:
            print("Vous ne faites aucun effort , il s'agirait de se ressaisir !!!!")
            return False




