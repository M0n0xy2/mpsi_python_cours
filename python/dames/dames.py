# -*- coding: UTF-8 -*-

import sys
import time

def main(argv):
    out = sys.stdout
    sizes = []

    for arg in argv:
        sizes.append(int(arg))

    for size in sizes:
        answers = timeit(True, solve, size)
        printGrid(out, answers, size)
        #print(answers)


def isUnderAttack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        left, right = left-1, right+1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    return subSolve2(n, n)

def subSolve1(n, grid_size):
    if n == 0:
        return [[]]

    smaller_solutions = subSolve1(n-1, grid_size)
    return [solution+[(n,i+1)] for i in range(grid_size) for solution in smaller_solutions if not isUnderAttack(i+1, solution)]

def subSolve2(n, grid_size):
    if n == 0:
        return [[]]

    smaller_solutions = subSolve2(n-1, grid_size)
    new_solutions = []
    for i in range(grid_size):
        for solution in smaller_solutions:
            if not isUnderAttack(i+1, solution):
                new_solutions.append(solution+[(n, i+1)])

    return new_solutions


def printGrid(io_out, answers, size):
    horizontal_border = "+ {} +\n".format(" ".join([chr(l) for l in range(65, 65+size)]))

    sol_num = 0

    header = " Taille {0}*{0} : {1} solutions ".format(size, len(answers))
    to_print = "=" * 40 + "\n"
    to_print += "{:=^40}\n".format(header)
    to_print += "=" * 40 + "\n\n"


    for answer in answers:
        sol_num += 1
        to_print += "Taille {0}*{0} Solution {1} :\n".format(size, sol_num)
        to_print += horizontal_border
        for y in range(1, size + 1):
            to_print += "{:<2}".format(size + 1 - y)
            for x in range(1, size + 1):
                if (x, y) in answer:
                    to_print += "D "
                else:
                    to_print += "  "
            to_print += (str(size + 1 - y) + "\n")
        to_print += horizontal_border + "\n"

    io_out.write(to_print)

#just for timing
def timeit(print_time, f, *args, **kwargs):
    start = time.clock()
    ret = f(*args, **kwargs)
    elapsed = time.clock() - start;
    if print_time:
        if(elapsed > 1):
            print("Elapsed time : {}s".format(elapsed))
        else:
            print("Elapsed time : {}ms".format(elapsed * 1000))
    return ret

if __name__ == '__main__':
    main(sys.argv[1:])
