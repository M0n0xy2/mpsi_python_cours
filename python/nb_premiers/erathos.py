#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys
import math

def crible(maximum):
    maximum += 1
    working_list = [True] * maximum
    working_list[0:2] = [False]*2
    for i in range(2, int(math.sqrt(maximum))):
        if working_list[i]:
            for j in range(i ** 2, maximum):
                if j % i == 0:
                    working_list[j] = False
            
    return [pos for pos, value in enumerate(working_list) if value]
    # pairs = [(elem, elem + 2) for elem in prem if elem + 2 in prem]
    check0000 = [elem for elem in prem if "0000" in str(elem)]
    return check0000


def main(argv):
    if argv:
        print(*crible(int(argv[0])))

if __name__ == "__main__":
    main(sys.argv[1:])
