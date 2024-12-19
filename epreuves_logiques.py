def affiche_batonnets(n) :
    return print("|" * n)

def joueur_retrait(n) :
    n_retraits = int(input("Choisissez entre 1 et 3 batons a retirer."))
    while n_retraits > 3 or n_retraits == 0:
        print("Entrée invalide. Choisissez un nombre entre 1 et 3, et pas plus que le nombre restant.")
        n_retraits = int(input("Choisissez entre 1 et 3 batons a retirer."))
    return n_retraits

def maitre_retrait(n):
    n_retraits = n % 4
    if n_retraits == 0:
        n_retraits = 1
    return min(n_retraits, n)


def jeu_nim():
    total_batonnets = 20
    print("Bienvenue au jeu de Nim !")
    while total_batonnets > 0:
        affiche_batonnets(total_batonnets)

        # Tour du joueur
        retrait_joueur = joueur_retrait(total_batonnets)
        total_batonnets -= retrait_joueur
        if total_batonnets == 0:
            print("Vous avez perdu ! Le maître du jeu gagne.")
            break

        # Tour du maître
        retrait_maitre = maitre_retrait(total_batonnets)
        print(f"Le maître du jeu retire {retrait_maitre} bâtonnets.")
        total_batonnets -= retrait_maitre
        if total_batonnets == 0:
            print("Le maître du jeu a perdu ! Vous gagnez.")
            break
s