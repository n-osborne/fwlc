#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: testInput.py
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018; febuary

:synopsis: test weihter a string is a well formed candidate for lread.buildTree
Finite State Machine with four states.

:Tests:

>>> initParsing("(xy)")
True
>>> initParsing("(/x.(xy)(x(ud)))")
True
>>> initParsing("((/r.r)z)")
True
>>> initParsing("((zy)((xy)e))")
True
>>> initParsing("()")
False
>>> initParsing("(Xy)")
False
>>> intiParsing("((xy)z")
False
>>> initParsing("(xy)z)")
False
>>> initParsing("(xyz)")
False
>>> intiParsing("(/x(xy))")
False
"""


import alphabet_def

var = alphabet_def.VAR_SET
op = alphabet_def.POSSIBLE_OP
dot = alphabet_def.LAMBDA_DOT








def initParsing(candidate):
    """
    Initialize the test.

    :param candidate: the string to parse
    :type candidate: str
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """
    if type(candidate) == str and candidate in var:
        return True

    elif type(candidate) != str\
       or len(candidate) < 4\
       or candidate[0] != '('\
       or not set(candidate).issubset(alphabet_def.TOTAL_ALPHABET):
        return False

    else:
        return parse(candidate, 0)















if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
