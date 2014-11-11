# -*- coding: UTF-8 -*-

import sys


def random_word():
    return "vache"


def request_name():
    return input("Votre nom : ")


def main(argv):
    name = request_name()
    word = [[c, False] for c in random_word()]
    tried = []
    score = 8
    while score > 0:
        w = ""
        for (c, f) in word:
            w += c if f else "*"
        print("(Score : {})  Mot à trouver : {}".format(score, w))

        t = ""
        while len(t) != 1 and t not in tried:
            t = input("Merci de rentrer une nouvelle lettre : ")
        tried.append(t)
        won = False
        for i in range(len(word)):
            if word[i][0] == t:
                word[i][1] = True
                won = True
        if not won:
            score -= 1
        for (_, t) in word:
            if t:


    if score == 0:
        print("You loose")
    else:
        print("You won")



if __name__ == '__main__':
    main(sys.argv[1:])
