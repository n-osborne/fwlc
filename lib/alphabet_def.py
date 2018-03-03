#!/usr/bin/env python3

from string import ascii_lowercase

VAR_SET = set(ascii_lowercase)
POSSIBLE_OP = (chr(955), '/')
# for representation:
LAMBDA_OP = POSSIBLE_OP[0]
LAMBDA_DOT = '.'
TOTAL_ALPHABET = VAR_SET.union(set(POSSIBLE_OP).union(set(LAMBDA_DOT)))
