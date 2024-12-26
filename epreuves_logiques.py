# Fonction qui affiche les bâtonnets restants
def affiche_batonnets(n) :
    return print("|" * n)

def joueur_retrait(n) :
    # Demande au joueur de choisir un nombre de bâtonnets à retirer
    n_retraits = int(input("Choisissez entre 1 et 3 batons a retirer."))
    # Valider l'entrée utilisateur
    while n_retraits > 3 or n_retraits == 0:
        print("Entrée invalide. Choisissez un nombre entre 1 et 3, et pas plus que le nombre restant.")
        n_retraits = int(input("Choisissez entre 1 et 3 batons a retirer."))
    return n_retraits

# Fonction pour le maître du jeu qui joue de manière optimale
def maitre_retrait(n):
    # Stratégie : retirer un nombre qui laisse un multiple de 4 à l'adversaire
    n_retraits = n % 4
    # Si aucun retrait optimal, retirer 1 bâton par défaut.
    if n_retraits == 0:
        n_retraits = 1
    return min(n_retraits, n)

# Fonction principale qui implémente le jeu de Nim
def jeu_nim():
    total_batonnets = 20
    print("Bienvenue au jeu de Nim !")
    while total_batonnets > 0:
        # Boucle principale du jeu
        affiche_batonnets(total_batonnets)
        #g
        # Tour du joueur
        retrait_joueur = joueur_retrait(total_batonnets)
        print("Combien de batonnets voulez-vous retirer (1, 2 ou 3) ?", retrait_joueur)
        total_batonnets -= retrait_joueur # Met à jour le total de bâtonnets
        if total_batonnets == 0: # Vérifie si le joueur a perdu
            print("Vous avez perdu ! Le maître du jeu gagne.")
            return False
        else :
            print("Batonnets restants : ", total_batonnets)

        # Tour du maître
        retrait_maitre = maitre_retrait(total_batonnets)
        print(f"Le maître du jeu retire {retrait_maitre} bâtonnets.")
        total_batonnets -= retrait_maitre # Met à jour le total de bâtonnets
        if total_batonnets == 0: # Vérifie si l'ordinateur a perdu
            print("Le maître du jeu a retiré le dernier bâtonnet ! Le joueur gagne.")
            return True
        else :
            print("Batonnets restants : ", total_batonnets)


