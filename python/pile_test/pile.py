#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys

class Pile:
    def __init__(self, X=None):
        if not X:
            X = []
        self.contenu = X
    def is_empty(self):
        return len(self.contenu) == 0
    def empiler(self, x):
        self.contenu.append(x)
    def depiler(self):
        return self.contenu.pop()
    def trier(self):
        for i in range(1, len(self.contenu)):
            x = self.contenu[i]
            j = i
            while j > 0 and self.contenu[j - 1] > x:
                self.contenu[j] = self.contenu[j - 1]
                j -= 1
            self.contenu[j] = x    
    def __str__(self):
        to_print = ""
        for elem in self.contenu:
            to_print += "[{!s}".format(elem)
        return to_print

    def __repr__(self):
        return self.__str__()

def main(argv):
    p = Pile([])
    p.empiler(1)
    p.empiler(2)
    p.empiler(4)
    p.empiler(3)
    p.empiler(7)
    p.empiler(9)
    p.empiler(18)
    print(p)
    p.trier()
    print(p)
    print(p.depiler())


if __name__ == "__main__":
    main(sys.argv[1:])
