#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import operator
import enum
import string


# Exercice 1

class TokenKind(enum.Enum):
    operator = 1
    digit = 2
    identifier = 3
    symbol = 4


def LexingError(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class Token:
    @classmethod
    def factory(cls, expr):
        ope_dict = {
            "+": operator.__add__,
            "-": operator.__sub__,
            "*": operator.__mul__,
            "//": operator.__floordiv__,
            "%": operator.__mod__
        }

        if expr in ope_dict:
            kind = TokenKind.operator
            value = ope_dict[expr]
        elif expr.isdecimal():
            kind = TokenKind.digit
            value = int(expr)
        elif expr.isidentifier():
            kind = TokenKind.identifier
            value = expr
        else:
            raise LexingError(expr, "Unknown token")
        return Token(kind, value)

    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return "(value: {}, type: {})".format(self.value, self.kind)

    def __repr__(self):
        return self.__str__()


class Tokenizer:
    def __init__(self, input_str):
        self.input_str = input_str
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.input_str):
            raise StopIteration

        while self.input_str[self.pos] in string.whitespace:
            self.pos += 1

        word = str()
        for c in self.input_str[self.pos:]:
            if c in string.whitespace:
                break
            word += c
            self.pos += 1
        return Token.factory(word)


def val_NPI(lexer):
    memory = {}
    stack = []
    for tok in lexer:
        if tok.kind == TokenKind.operator:
            ope2 = stack.pop()
            ope1 = stack.pop()
            stack.append(tok.value(ope1, ope2))
        elif tok.kind == TokenKind.identifier:
            if tok.value not in memory:
                raise RuntimeError("Can't find {}'s value".format(tok.value))
            stack.append(memory[tok.value])
        else:
            stack.append(tok.value)
    return stack.pop()


def exo1():
    lexer = Tokenizer("34 13 + 5 *")
    print(val_NPI(lexer))


if __name__ == "__main__":
    exo1()
