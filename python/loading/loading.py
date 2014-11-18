# -*- coding: utf_8 -*-

import sys

class Loading:
    def __init__(self, maximum):
        self.__maximum = maximum
        self.__value = 0

    def progress(self, offset):
        self.__value += offset

    def value(self, value):
        self.__value += value

def main(argv):
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
