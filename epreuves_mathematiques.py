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













