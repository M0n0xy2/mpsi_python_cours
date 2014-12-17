#!/usr/bin/env python3
# -*- coding: utf_8 -*-
# **************************
# PCSIB DM2 2015
# Nom: Dizier Charles
# ***************************

import sys
import string


def fich2ch(chemin):
    """
        Retourne le contenu du fichier passé en argument

        arguments:
            chemin: fichier à lire
    """
    try:
        f = open(chemin, "r")
        t = f.read()
        f.close()
        return t
    except:
        print("Erreur à l'ouverture du fichier")
        sys.exit(1)


def signature(texte):
    """
        Retourne un dictionnaire contenant les fréquences d'apparition des 26
        lettres dans la chaine de caractères passée en argument

        arguments:
            texte: chaine de caractères à analyser
    """
    stats = {c: 0 for c in string.ascii_lowercase}
    counter = 0
    for c in texte:
        if c in string.ascii_letters:
            stats[c.lower()] += 1
            counter += 1

    return {l: stats[l] / counter for l in string.ascii_lowercase}


def affichesign(sign):
    """
        Affiche proprement la signature d’un texte en présentant les fréquences
        d'apparition des 26 lettres en colonne dans l’ordre alphabétique.
        Les fréquences sont données avec 6 chiffres après la virgule.

        arguments:
            sign: signature du texte à afficher
    """
    buf = ""
    for letter in string.ascii_lowercase:
        buf += "{} : {:.6f}\n".format(letter.upper(), sign[letter])
    print(buf)


def nettoiefrench(texte):
    """
        Retourne le texte donné en entrée sans les curiosités typographiques
        que possèdent le français et pas l’anglais

        arguments:
            texte: chaine de caractères à nettoyer
    """
    accents = {
        "à": "a",
        "â": "a",
        "ä": "a",
        "ç": "c",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ë": "e",
        "î": "i",
        "ï": "i",
        "ô": "o",
        "ö": "o",
        "ù": "u",
        "û": "u",
        "ü": "u",
        "æ": "ae",
        "œ": "oe",
        "À": "A",
        "Â": "A",
        "Ä": "A",
        "Ç": "C",
        "É": "E",
        "È": "E",
        "Ê": "E",
        "Ë": "E",
        "Î": "I",
        "Ï": "I",
        "Ô": "O",
        "Ö": "O",
        "Ù": "U",
        "Û": "U",
        "Ü": "U",
        "Æ": "AE",
        "Œ": "OE"
    }
    modified_texte = ""
    for letter in texte:
        if letter in accents:
            modified_texte += accents[letter]
        else:
            modified_texte += letter
    return modified_texte


def score(sign, ref_sign):
    """
        Retourne le score, c'est à dire l'ecart entre les signatures du texte
        en cours d'analyse et un texte de référence

        arguments:
            sign: signature du texte en cours d'analyse
            ref_sign: signature du texte de référence
    """
    return sum([abs(sign[l]-ref_sign[l]) for l in string.ascii_lowercase])


fr_sign = signature(nettoiefrench(fich2ch("vivelarepublique.txt")))
en_sign = signature(fich2ch("churchill.txt"))


def determinelangue(chemin):
    """
        Determine et affiche la langue du texte contenu dans le fichier à
        l'adresse passée en argument

        arguments:
            chemin: le chemin vers le fichier à analyser
    """
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
