#!/usr/bin/env python3
# -*- coding: utf_8 -*-

from random import randint
from time import sleep


def afficher(liste=[" ."]*9):
    n = int(len(liste) ** .5)
    L1 = "{:2} " + "|{:2} " * (n-1) + "\n"
    L2 = "---" + "+---" * (n-1) + "\n"
    Grille = L1 + (L2 + L1) * (n-1)
    print(Grille.format(*liste) + "\n" * 20)


def proposer(x, y, n, interdit):
    poss = []
    deplacements = [
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1)
    ]
    for dx, dy in deplacements:
        if 0 <= x+dx < n and 0 <= y+dy < n and (x+dx, y+dy) not in interdit:
            poss.append((dx, dy))
    return poss


def choisir(poss):
    return poss[randint(0, len(poss)-1)]


def attendre(attente):
    sleep(attente)


def pause():
    input("Appuyez sur <Entrée> pour continuer; Ctrl + C pour arreter")
    print("\n"*20)


def course(n=6, voir=3, attente=0.2):
    global POSITION
    tour, POSITION, historique, (x, y) = 0, [" ."]*(n**2), [], (0, 0)
    while True:
        tour += 1
        POSITION[x + y * n] = tour
        historique.append((x, y))
        if voir >= 3:
            afficher(POSITION)
        if voir == 3:
            attendre(attente)
        elif voir == 4:
            input()

        possibilites = proposer(x, y, n, historique)
        if possibilites:
            dx, dy = choisir(possibilites)
            x += dx
            y += dy
        else:
            POSITION[0] = tour
            POSITION[x + y * n] = "#"
            break

    if voir >= 1:
        afficher(POSITION)
    if voir >= 2:
        pause()
    return tour


def jeu(n=6, voir=3, attente=0.2):
    global POSITION

    POSITION = None
    record_max, record_min = 0, n**2
    while True:
        essai = course(n, voir, attente)
        if essai >= record_max:
            record_max = essai
            print("Record max battu !")
            afficher(POSITION)
            pause()
        if essai <= record_min:
            record_min = essai
            print("Record min battu !")
            afficher(POSITION)
            pause()


if __name__ == "__main__":
    jeu(n=8, voir=0)
