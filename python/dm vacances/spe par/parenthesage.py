# -*- coding: UTF-8 -*-

import random

catalan_memo = {}


def catalan(n):
    """retourne le n-ieme nombre de Catalan"""
    assert n >= 0, "n doit etre positif"

    if n == 0:
        return 1

    if n in catalan_memo:
        return catalan_memo[n]

    catalan_memo[n] = sum([catalan(i)*catalan(n-1-i) for i in range(n)])
    return catalan_memo[n]


def creer_mot(n):
    """creer un mot de parentheses de validite aleatoire de taille n"""
    word = str()
    for i in range(n):
        word += "(" if random.randint(0, 1) == 0 else ")"
    return word


def creer_bon_mot(n):
    """creer un mot de parentheses de validite vrai de taille 2n"""
    word = str()
    open_stack = ["("] * n
    close_stack = [")"] * n

    for i in range(n * 2):
        if len(open_stack) == 0:
            word += close_stack.pop()
        elif len(open_stack) >= len(close_stack):
            word += open_stack.pop()
        elif random.randint(0, 1):
            word += open_stack.pop()
        else:
            word += close_stack.pop()

    return word


def est_bien_par_pile(word):
    """verifie la validite d'un mot donne (par pile)"""
    stack = []
    for c in word:
        if c == "(":
            stack.append(c)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()
    return len(stack) == 0


def est_bien_par_no_pile(word):
    """verifie la validite d'un mot donne (par accumulateur)"""
    value = 0
    for c in word:
        if c == "(":
            value += 1
        elif value == 0:
            return False
        else:
            value -= 1
    return value == 0


def couple_par(word):
    """retourne les positions de chaques couples de parentheses"""
    if not is_well_formed_stack(word):
        return []

    stack = []
    list = []
    for pos, c in enumerate(word):
        if c == "(":
            stack.append(pos)
        else:
            list.append((stack.pop(), pos))
    return list


def dic_partiel(n):
    """retourne un dictionnaire partiel de mot de taille n correctement parenthese"""
    if n <= 0:
        return [""]
    elif n == 1:
        return ["()"]

    sub_list = dic_partiel(n-1)
    new_list = []
    for word in sub_list:
        new_list.append(word + "()")
        new_list.append("(" + word + ")")
    return new_list


def dictio(n):
    """retourne un dictionnaire complet de mot de taille n correctement parenthese"""
    if n == 0:
        yield str()
    else:
        for k in range(n):
            for mot1 in dictio(k):
                for mot2 in dictio(n-1-k):
                    yield "(" + mot1 + ")" + mot2


def time_me(func, *args, **kwargs):
    """fonction de monitoring"""
    start_t = time.time()
    ret = func(*args, **kwargs)
    end_t = time.time()
    return ret, end_t-start_t


def aide():
    """fonction d'aide"""
    for pgm, func in globals().items():
        if hasattr(func, '__call__'):
            if not func.__doc__:
                func.__doc__ = ""
            print(" - {:20} : {}".format(pgm, func.__doc__))


if __name__ == '__main__':
    aide()
