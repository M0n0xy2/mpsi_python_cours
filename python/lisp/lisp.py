#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys
import operator
import enum
import string


# Exercice 1

class TokenKind(enum.Enum):
    operator = 1
    digit = 2
    identifier = 3


class LexingError(Exception):
    def __init__(self, msg):
        self.msg = str(msg)

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.__str__()


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return "(value: {}, type: {})".format(self.value, self.kind)

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, input_str):
        self.input_str = input_str.strip() + "\n"
        self.pos = 0
        self.ope_dict = {
            "+": operator.__add__,
            "-": operator.__sub__,
            "*": operator.__mul__,
            "/": operator.__floordiv__,
            "%": operator.__mod__
        }

    def __iter__(self):
        return self

    def __next__(self):
        self._eat_whitespace()
        if self._at_end():
            self.pos = -1
            raise StopIteration

        if self.input_str[self.pos].isalpha():
            start_pos = self.pos
            self.pos += 1
            while self.input_str[self.pos].isalnum():
                self.pos += 1
            identifier = self.input_str[start_pos:self.pos]
            return Token(TokenKind.identifier, identifier)
        elif self.input_str[self.pos].isdecimal():
            start_pos = self.pos
            self.pos += 1
            while self.input_str[self.pos].isdecimal():
                self.pos += 1
            digit = int(self.input_str[start_pos:self.pos])
            return Token(TokenKind.digit, digit)
        elif self.input_str[self.pos] in "+-*%/":
            oper = self.input_str[self.pos]
            self.pos += 1
            return Token(TokenKind.operator, self.ope_dict[oper])
        else:
            wtf_char = self.input_str[self.pos]
            raise LexingError("Unknown char '{}'".format(wtf_char))

    def _at_end(self):
        return self.pos == len(self.input_str)

    def _eat_whitespace(self):
        while self.input_str[self.pos] in string.whitespace:
            self.pos += 1
            if self._at_end():
                raise StopIteration


def evaluate(lexer):
    memory = {}
    stack = []
    for tok in lexer:
        if tok.kind == TokenKind.operator:
            if len(stack) < 2:
                raise RuntimeError("Your expression is not well formed")
            ope2, ope1 = stack.pop(), stack.pop()
            stack.append(tok.value(ope1, ope2))
        elif tok.kind == TokenKind.identifier:
            if tok.value not in memory:
                raise RuntimeError("Can't find {}'s value".format(tok.value))
            stack.append(memory[tok.value])
        else:
            stack.append(tok.value)
    return stack.pop()


def main(argv):
    while True:
        expr = ""
        while not expr:
            expr = input("[NPI]>> ")
            if expr == "exit":
                return
        try:
            result = evaluate(Lexer(expr))
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main(sys.argv[1:])
