#!/usr/bin/env python3
# -*- coding: utf_8 -*-
# **************************
# PCSIB DM2 2015
# Nom: Dizier Charles
# ***************************

import sys
import string
import unicodedata


def fich2ch(chemin):
    try:
        f = open(chemin, "r")
        t = f.read()
        f.close()
        return t
    except:
        print("Erreur à l'ouverture du fichier")
        sys.exit(1)


def signature(texte):
    stats = {c: 0 for c in string.ascii_lowercase}
    counter = 0
    for c in texte:
        if c in string.ascii_letters:
            stats[c.lower()] += 1
            counter += 1

    return {l: stats[l] / counter for l in string.ascii_lowercase}


def affichesign(sign):
    buf = ""
    for letter in string.ascii_lowercase:
        buf += "{} : {:.6f}\n".format(letter.upper(), sign[letter])
    print(buf)


def nettoiefrench(texte):
    return str(unicodedata.normalize("NFKD", texte).encode("ascii", "ignore"))


def score(sign, ref_sign):
    return sum([abs(sign[l]-ref_sign[l]) for l in string.ascii_lowercase])


fr_sign = signature(nettoiefrench(fich2ch("vivelarepublique.txt")))
en_sign = signature(fich2ch("churchill.txt"))


def determinelangue(chemin):
    test_sign = signature(nettoiefrench(fich2ch(chemin)))
    fr_score = score(test_sign, fr_sign)
    en_score = score(test_sign, en_sign)
    if en_score < fr_score:
        print("Ce document est en Anglais")
    elif fr_score < en_score:
        print("Ce document est en Français")
    else:
        print("Je ne suis pas capable de detecter la langue de ce texte")


if __name__ == "__main__":
    affichesign(en_sign)
    determinelangue("inconnu.txt")
    determinelangue("inconnu2.txt")
