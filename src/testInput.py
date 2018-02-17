#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: testInput.py
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018; febuary

:synopsis: test weihter a string is a well formed candidate for lread.buildTree
Finite State Machine with five states.

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
opening = '('
closing = ')'





def initParsing(candidate):
    """
    Initialize the test.

    :param candidate: the string to parse
    :type candidate: str
    :return: true if candidate is well formed, false otherwise
    :rtype: bool
    """

    if type(candidate) != str:
        return False
    else:
        return varOrOpening(iter(candidate), 0)



    
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
        if char == closing:
            return anythingButOp(candidate, cpt-1)
        elif char == opening:
            return anythingButClosing(candidate, cpt+1)
        elif char in var:
            return varOrClosing(candidate, cpt)
        else: # char is dot, in op or not in alphabet
            return False
        
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
        if char == opening:
            return anythingButClosing(candidate, cpt+1)
        elif char in var:
            return varOrOpening(candidate, cpt)
        elif char in op:
            binder = next(candidate)
            point = next(candidate)
            if binder in var and point == dot:
                return varOrOpening(candidate, cpt)
            else:
                return False
        else: # char is closing, dot or not in the alphabet
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
        if char in var:
            return onlyClosing(candidate, cpt)
        elif char == opening:
            return anythingButClosing(candidate, cpt+1)
        else: # char is op or closing or dot or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0




def varOrClosing(candidate, cpt):
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
        if char == closing:
            return anythingButOp(candidate, cpt-1)
        elif char in var:
            return onlyClosing(candidate, cpt)
        else: # char is op, dot, opening or not in the alphabet
            return False

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
        if char == closing:
            return anythingButOp(candidate, cpt-1)
        else: # char is opening, in var, op or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0




















if __name__ == '__main__':
    import doctest
    doctest.testmod()
