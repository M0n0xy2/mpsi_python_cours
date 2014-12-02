#!/usr/bin/env python3

import sys


class Board:
    jumps = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1)
    ]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]

    def in_range_and_empty(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height \
            and self.board[x][y] == 0

    def fill(self, x, y, counter):
        assert self.board[x][y] == 0
        self.board[x][y] = counter
        if counter == self.width * self.height:
            self.print_out()
            sys.exit()
        for jump in self.jumps:
            tx, ty = x + jump[0], y + jump[1]
            if self.in_range_and_empty(tx, ty):
                self.fill(tx, ty, counter+1)
        self.board[x][y] = 0

    def print_out(self):
        scale = len(str(self.width * self.height))
        line_sep = ("+" + scale * "-") * self.width + "+\n"
        to_print = line_sep
        for y in range(self.height):
            for x in range(self.width):
                to_print += "|{}".format(str(self.board[x][y]).rjust(scale))
            to_print += "|\n" + line_sep
        print(to_print)


def usage(path):
    print("Usage: {} <width>")
    sys.exit(1)


def main(argv):
    if len(argv) == 1:
        usage(sys.argv[0])
    try:
        if len(argv) == 2:
            width = height = int(sys.argv[1])
        else:
            width = int(sys.argv[1])
            height = int(sys.argv[2])
    except:
        usage(sys.argv[0])

    board = Board(width, height)
    board.fill(0, 0, 1)


if __name__ == "__main__":
    main(sys.argv)
