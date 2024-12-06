import random
a = random.randint(1,10)
b = random.randint(1,10)
def resoudre_equation_lineaire(a,b):
    x = -b/a
    return a,b,x

S=False
def epreuve_math_equation():
    global a,b,S
    a, b, x = resoudre_equation_lineaire(a,b)
    print("Resoudre : ",a,"x +", b, "=", 0)
    X=float(input("Saisir la solution X :"))
    if x == X:
        S=True
    return S
S=epreuve_math_equation()
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

def premier_plus_proche(n):
    n = random.randint(10,20)
    reponse = int(input("veuillez saisir l'entier supérieur premier le plus proche de n"))
    premier_plus_proche(n)
    if n == reponse:
        print("Bravo vous etes le meilleur vous venez de remporter une clef")
        return True
    else:
        print("Il s'agirait de faire des efforts vous etes en école d'ingénieur. Vous venez de perdre une clée")
        return False
