#!/usr/bin/env python3
#probleme des 8 dames

def printGrid(grid):
    for y in range(8):
        print(8 - y, end=" |")
        for x in range(8):
            print(grid[x][y], "", end="")
        print()
    print("------------------")
    print("X |A B C D E F G H")

grid = [[0] * 8 for _ in range(8)]
for j in range(8):
    for i in range(8):
        grid[i][j] = (i + j) % 10
printGrid(grid)
