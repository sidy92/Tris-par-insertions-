#TRI PAR INSERTION

#cette algorithme consiste à insérert à chaque étape l’élément d’indice j dans la partie d'un tableau déjà triée, comme un joueur de cartes insérant dans son jeu trié les cartes au fur et à mesure qu’il les reçoit.


def insere(t, j):
    k = j
    while k > 0 and t[k] < t[k−1]:
        t[k−1], t[k] = t[k], t[k−1]
        k −= 1

#On justifie la validité de cette fonction en prouvant l’invariant : à l’entrée de la boucle d’indice k > 0 les tableaux t[0 : k] et t[k : j + 1] sont triés


def insere(t, j):
    k, a = j, t[j]
    while k > 0 and t[k] < t[k−1]:
        t[k] = t[k−1]
        k −= 1
    t[k] = a


def insertion_sort(t):
    for j in range(1, len(t)):
        insere(t, j)

#On justifie la validité de cette fonction en prouvant l’invariant : à l’entrée de la boucle d’indice j le tableau t[0 : j] est trié.