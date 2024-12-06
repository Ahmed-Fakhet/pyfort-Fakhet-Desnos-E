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







