# -*- coding: utf-8 -*-
# ***************************
# PCSIB DM3 2015
# Nom: Dizier Charles
# ****************************

import random

equi_num_object = {
    1: "pierre",
    2: "papier",
    3: "ciseaux",
    4: "lezard",
    5: "spock"
}

winner_dict = {
    "papier, ciseaux": False,
    "ciseaux, papier": True,
    "papier, pierre": True,
    "pierre, papier": False,
    "pierre, lezard": True,
    "lezard, pierre": False,
    "lezard, spock": True,
    "spock, lezard": False,
    "spock, ciseaux": True,
    "ciseaux, spock": False,
    "lezard, ciseaux": False,
    "ciseaux, lezard": True,
    "papier, lezard": False,
    "lezard, papier": True,
    "papier, spock": True,
    "spock, papier": False,
    "spock, pierre": True,
    "pierre, spock": False,
    "pierre, ciseaux": True,
    "ciseaux, pierre": True
}


def combat(player, ia):
    global ia_score, player_score
    combat_str = "{}, {}".format(equi_num_object[player], equi_num_object[ia])
    player_winner = winner_dict[combat_str]
    if player_winner:
        player_score += 1
    elif not player_winner:
        ia_score += 1


def enregistrevainqueur():
    out_file = open("resultatsPPCLS.txt", "a")
    if ia_score > player_score:
        winner = '"IA"'
        winner_score, looser_score = ia_score, player_score
    else:
        winner = '"Joueur"'
        winner_score, looser_score = player_score, ia_score
    print("Vainqueur : {} sur un score de {} contre {} points".format(winner, winner_score, looser_score), file=out_file)


if __name__ == "__main__":
    ia_score = 0
    player_score = 0
    while ia_score < 5 and player_score < 5:
        print("Choix de jeu :")
        for num, obj in equi_num_object.items():
            print("{} pour {}".format(num, obj))
        player_play = int(input('Entrez 1,2,3,4 ou 5 selon votre choix de jeu: '))
        ia_play = random.randint(1, 5)
        if player_play == ia_play:
            print("Egalité ! On recommence")
            continue
        combat(player_play, ia_play)
        print("===================")
        print("Scores actuels : ")
        print("Joueur: {} point(s)".format(player_score))
        print("IA: {} point(s)".format(ia_score))
        print("===================")
    enregistrevainqueur()
