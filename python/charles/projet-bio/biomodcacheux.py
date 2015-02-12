# -*- coding: utf-8 -*-
# ***************************
# PCSIB DM4bio 2015
# Nom: Cacheux Paul
# ****************************


def freqADN(adn):
    frequ = {"A": 0, "T": 0, "C": 0, "G": 0}
    for base in adn:
        frequ[base] += 1
    for base in "ATCG":
        frequ[base] /= len(adn)
    return frequ


def ADN2arn(adn):
    arn = ""
    for base in adn:
        if base == "T":
            arn += "u"
        else:
            arn += base.lower()
    return arn


def arn2prot(arn):
    equi = {
        "gcu": "A",
        "gcc": "A",
        "gca": "A",
        "gcg": "A",
        "ugu": "C",
        "ugc": "C",
        "gau": "D",
        "gac": "D",
        "gaa": "E",
        "gag": "E",
        "uuu": "F",
        "uuc": "F",
        "ggu": "G",
        "ggc": "G",
        "gga": "G",
        "ggg": "G",
        "cau": "H",
        "cac": "H",
        "auu": "I",
        "auc": "I",
        "aua": "I",
        "aaa": "K",
        "aag": "K",
        "uua": "L",
        "uug": "L",
        "cuu": "L",
        "cuc": "L",
        "cua": "L",
        "cug": "L",
        "aug": "M",
        "aau": "N",
        "aac": "N",
        "uag": "O",
        "ccu": "P",
        "ccc": "P",
        "cca": "P",
        "ccg": "P",
        "caa": "Q",
        "cag": "Q",
        "cgu": "R",
        "cgc": "R",
        "cga": "R",
        "cgg": "R",
        "aga": "R",
        "agg": "R",
        "ucu": "S",
        "ucc": "S",
        "uca": "S",
        "ucg": "S",
        "agu": "S",
        "agc": "S",
        "acu": "T",
        "acc": "T",
        "aca": "T",
        "acg": "T",
        "uga": "U",
        "guu": "V",
        "guc": "V",
        "gua": "V",
        "gug": "V",
        "ugg": "W",
        "uau": "Y",
        "uac": "Y",
    }

    prot = ""
    for i in range(0, len(arn), 3):
        codon = arn[i:i+3]
        prot += equi[codon]
    return prot


def fich2ADN(path):
    fich = open(path, "r")
    fich.readline()  # afin de supprimer la ligne d'en-tete
    adn = ""
    for line in fich:
        adn += line.rstrip("\n\r")
    return adn


def muta(std, mut):
    std_adn = fich2ADN(std)
    mut_adn = fich2ADN(mut)

    assert len(std_adn) == len(mut_adn), "sequencies must be equals"

    mutations = []
    for i in range(len(std_adn)):
        print(i, std_adn[i], mut_adn[i])
        if std_adn[i] != mut_adn[i]:
            mutations.append((i, std_adn[i], mut_adn[i]))
    return mutations
