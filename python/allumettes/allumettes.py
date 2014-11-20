#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys
import random


def print_allumettes(n):
    """Fonction simple qui affiche les allumettes (juste du design)"""
    to_print = "\n"
    to_print += "  " + "*"*n + "\n"
    to_print += "  " + "|"*n + "\n"
    # to_print += "  " + "|"*n + "\n"
    print(to_print)


class Player:
    """
        classe abstraite qui permet de representer un joueur sous toutes
        ses formes
    """
    def __init__(self, name):
        self.name = name

    def play(self, max, on_board):
        raise NotImplementedError

    def you_win(self):
        raise NotImplementedError

    def you_loose(self):
        raise NotImplementedError


class RealPlayer(Player):
    """
        classe representant un vrai joueur
    """
    def play(self, max, on_board):
        print("[{}] C'est votre tour : il reste {} allumettes".format(self.name, on_board))
        print_allumettes(on_board)
        wish = 0
        while wish < 1 or wish > 3:
            wish = int(input("[{}] : Combien d'allumettes souhaitez vous jouer (entre 1 et 3) ? : ".format(self.name)))
        return wish

    def you_win(self):
        print("[{}] : Vous avez gagné !! Bien joué".format(self.name))

    def you_loose(self):
        print("[{}] : Vous avez perdu..".format(self.name))


class IAPlayer(Player):
    def play(self, max, on_board):
        print("[{} (IA)] C'est mon tour".format(self.name))
        wish = 3
        for i in range(3, 0, -1):
            if (on_board - i) % 4 == 1:
                wish = i
                break
        print("[{} (IA)] Je prend {} allumettes".format(self.name, wish))
        return wish

    def you_win(self):
        print("[{} (IA)] J'ai gagné..".format(self.name))

    def you_loose(self):
        print("[{} (IA)] J'ai perdu.. !!".format(self.name))


def game(lenght=30):
    on_board = lenght
    players = (RealPlayer("Joueur 1"), IAPlayer("IA 1"))
    actual_player = random.randint(0, 1)
    while on_board > 0:
        actual_player = 1 - actual_player
        on_board -= players[actual_player].play(lenght, on_board)
        if on_board <= 0:
            print("="*80)
            players[actual_player].you_loose()
            players[1 - actual_player].you_win()


def main(argv):
    game()


if __name__ == "__main__":
    main(sys.argv[1:])
