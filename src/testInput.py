#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: testInput.py
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018; febuary

:synopsis: test weihter a string is a well formed candidate for lread.buildTree
Finite State Machine with four states.

:Tests:

>>> initParsing("x")
True
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
>>> initParsing("((xy)z")
False
>>> initParsing("(xy)z)")
False
>>> initParsing("(xyz)")
False
>>> initParsing("(/x(xy))")
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
         or candidate[0] != '('\
         or len(candidate) < 4:
         # or not set(candidate).issubset(alphabet_def.TOTAL_ALPHABET):
        return False

    else:
        return anythingButOp(iter(candidate), 0)




    
def anythingButOp(candidate, cpt):
    """
    Read first letter of candidate and search for anything but op.
    
    :param candidate: the string to parse in an iterator
    :type candidate: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """
        
    try:
        char = next(candidate)
        # print(char)
        if char == op or char == dot:
            return False
        elif char == ')':
            return anythingButOp(candidate, cpt-1)
        elif char == '(':
            return anythingButClosing(candidate, cpt+1)
        else:
            return varOrOpening(candidate, cpt)
        
    except StopIteration:
        return cpt == 0
        



        
def anythingButClosing(candidate, cpt):
    """
    Read first letter of candidate and search for anything but op.
    
    :param candidate: the string to parse
    :type candidate: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(candidate)
        # print(char)
        if char == ')' or char == dot:
            return False
        elif char == '(':
            return anythingButClosing(candidate, cpt+1)
        elif char in var:
            return varOrOpening(candidate, cpt)
        else:
            binder = next(candidate)
            point = next(candidate)
            if binder in var and point == dot:
                return varOrOpening(candidate, cpt)
            else:
                return False

    except StopIteration:
        return cpt == 0






def varOrOpening(candidate, cpt):
    """
    Read first letter of candidate and search for anything but op.
    
    :param candidate: the string to parse
    :type candidate: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(candidate)
        # print(char)
        if char == op or char == ')' or char == dot:
            return False
        elif char in var:
            return onlyClosing(candidate, cpt)
        else:
            return anythingButClosing(candidate, cpt+1)

    except StopIteration:
        return cpt == 0






def onlyClosing(candidate, cpt):
    """
    Read first letter of candidate and search for anything but op.
    
    :param candidate: the string to parse
    :type candidate: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(candidate)
        # print(char)
        if char == ')':
            return anythingButOp(candidate, cpt-1)
        else:
            return False

    except StopIteration:
        return cpt == 0




















if __name__ == '__main__':
    import doctest
    doctest.testmod()
