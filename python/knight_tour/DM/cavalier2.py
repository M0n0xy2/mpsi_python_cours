#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# ====================================
# Paul Cacheux <paulcacheux@gmail.com>
# MPSI 1
# DM informatique
# 13/12/2014
# ====================================

from random import randint  # Module importé

N = 6
HISTORIQUE = []      # Variables globales


def afficher(last_move=(0, 0)):
    """ Dessine la grille  n x n """
    liste = [' .'] * (N**2)
    for i in range(len(HISTORIQUE)):
        (x, y) = HISTORIQUE[i]
        liste[x + y * N] = i

    if last_move != (0, 0):
        last_x = x + last_move[0]
        last_y = y + last_move[1]
        liste[last_x + last_y * N] = " :"

    Espace = "\n" * 15
    Titre = "TOUR {}. Cavalier en {}.\n\n".format(len(HISTORIQUE), (x, y))
    L1 = " " + ("|{:2} " * N)[1:] + "\n"
    L2 = " " + ("+---" * N)[1:] + "\n"
    Grille = (L1 + (L2 + L1) * (N-1)).format(*liste)
    print(Espace + Titre + Grille)


def proposer(x, y):
    """ Retourne sous forme de liste l'éventail des possibles. """
    poss = []
    for dx, dy in [
        (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]:
        if 0 <= x+dx < N and 0 <= y+dy < N and (x+dx, y+dy) not in HISTORIQUE:
            poss.append((dx, dy))
    return poss


def presenter(poss, last_move):
    """ Présenter les choix à l'utilisateur. """
    prop = "CHOIX :" + "\n"
    prop += "    espace : arrière" + "\n"
    prop += "    entrée : automatique" + "\n"
    prop += "    autre  : hasard" + "\n"

    for i, p in enumerate(poss):
        star = " "
        if last_move == p:
            star = "*"
        prop += "       {}{}:{}\n".format(star, i, p)
    prop += "\n" * (8 - len(poss))

    print(prop)


def choisir(poss, last_move):
    """ Choisir le mouvement. """
    reponse = input(" ? ")
    if reponse == "":
        if last_move == (0, 0):
            return poss[0]  # Choix automatique :
        try:
            return poss[poss.index(last_move) + 1]
        except:
            return (0, 0)

    if reponse in "_ ":
        return (0, 0)  # On demande un retour en arrière
    if reponse[0].lower() == "f":
        raise StopIteration
    try:
        return poss[int(reponse)]  # Choix de l'utilisateur
    except:
        return poss[randint(0, len(poss)-1)]  # Choix au hasard


def course_intelligente(x=0, y=0, manuel=False):
    """
        Faire avancer le cavalier autant que possible, automatiquement.
        Le mode manuel permet de voir les etapes une par une
    """
    HISTORIQUE.append((x, y))
    while len(HISTORIQUE) != N**2:
        if manuel:
            afficher()
            input()
        x, y = HISTORIQUE[-1]
        possibilities = proposer(x, y)
        best_score = 10  # plus que 8
        new_x, new_y = 0, 0
        # on recherche le plus petit nombre de possibilités à l'etat suivant
        for poss in possibilities:
            score = len(proposer(x + poss[0], y + poss[1]))
            if score <= best_score:
                best_score = score
                new_x = x + poss[0]
                new_y = y + poss[1]
        HISTORIQUE.append((new_x, new_y))
    afficher()
    print("Tour fini !!")


def course(x=0, y=0):
    """ Faire avancer le cavalier autant que possible. """
    HISTORIQUE.append((x, y))
    last_move = (0, 0)
    afficher(last_move)

    while True:
        (x, y) = HISTORIQUE[-1]
        poss = proposer(x, y)

        if poss == []:
            input("BLOQUE ! Seul choix possible : arrière." + "\n" * 13)
            (dx, dy) = (0, 0)  # on est coincé, donc : retour en arrière
        else:
            presenter(poss, last_move)
            try:
                (dx, dy) = choisir(poss, last_move)
            except StopIteration:
                break

        if (dx, dy) == (0, 0):  # Retour en arrière
            if len(HISTORIQUE) > 1:  # Seulement si c'est possible !
                rem_x, rem_y = HISTORIQUE.pop()
                new_x = rem_x - HISTORIQUE[-1][0]
                new_y = rem_y - HISTORIQUE[-1][1]
                last_move = (new_x, new_y)
        else:
            HISTORIQUE.append((x + dx, y + dy))
            last_move = (0, 0)

        afficher(last_move)
    print("Fin")


if __name__ == '__main__':  # ==============MAIN==============
    print("Par défaut, la taille de la grille est de 6 * 6.")
    print("   - pour garder cette valeur, appuyer sur entrée,")
    p = input("   - sinon, proposer une valeur : ")
    try:
        assert 2 < int(p) < 12
        N = int(p)
    except:
        pass
    course_intelligente(manuel=True)
