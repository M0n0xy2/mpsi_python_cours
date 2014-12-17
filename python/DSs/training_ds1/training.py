# -*- coding: utf_8 -*-

import sys
import string


def isalpha(str):
    for c in str:
        if c not in string.ascii_letters:
            return False
    return True


def remove_double(L):
    last = None
    ret = []
    for elem in sorted(L):
        if elem != last:
            ret.append(elem)
            last = elem
    return ret


def anagrammes(mot):

    def anagrammes_sub(mot):
        anagrammes_sub.__compteur += 1
        print("->", mot)
        if len(mot) <= 1:
            return [mot]
        elif len(mot) == 2:
            return list(set([mot, mot[::-1]]))
        else:
            return list(set(
                [mot[i] + ana
                    for i in range(len(mot))
                    for ana in anagrammes_sub(mot[:i] + mot[i+1:])]
                ))
    anagrammes_sub.__compteur = 0
    return anagrammes_sub(mot), anagrammes_sub.__compteur


def main(argv):
    mot = ""

    while len(mot) < 3 or not isalpha(mot):
        mot = input("Veuillez entrer un mot d'au moins 3 caractéres : ")
        if not mot:
            print("A bientot !")
            sys.exit()

    mot = mot.upper()
    print("Les anagrammes de \"{}\" sont : ".format(mot))
    ana = anagrammes(mot)
    print(len(ana[0]))
    print(*ana[0], sep="\n")
    print("Profondeur maximale : {}".format(ana[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
