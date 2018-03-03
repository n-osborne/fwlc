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
>>> initParsing("(xy)(zt)")
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
    elif candidate in var:
        return True
    else:
        iteration = iter(candidate)
        char = next(iteration)
        if char != opening:
            return False
        else:
            return anythingButClosing(iteration, 1)






def varOrOpening(iteration, cpt):
    """
    Take one step in the iterator and search for var or opening.
    
    :param iteration: the string to parse
    :type iteration: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if iteration is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(iteration)
        if cpt == 0:
            return False
        elif char in var:
            return onlyClosing(iteration, cpt)
        elif char == opening:
            return anythingButClosing(iteration, cpt+1)
        else: # char is op or closing or dot or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0







        
def anythingButClosing(iteration, cpt):
    """
    Take one step in the iterator and search for anything but closing.
    
    :param iteration: the string to parse
    :type iteration: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if iteration is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(iteration)
        if cpt == 0:
            return False
        elif char == opening:
            return anythingButClosing(iteration, cpt+1)
        elif char in var:
            return varOrOpening(iteration, cpt)
        elif char in op:
            binder = next(iteration)
            point = next(iteration)
            if binder in var and point == dot:
                return varOrOpening(iteration, cpt)
            else:
                return False
        else: # char is closing, dot or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0





    
def anythingButOp(iteration, cpt):
    """
    Take one step in the iterator and search for anything but op.
    
    :param iteration: the string to parse in an iterator
    :type iteration: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if iteration is well formed, false otherwise
    :rtype: bool
    """
        
    try:
        char = next(iteration)
        if cpt == 0:
            return False
        elif char == closing:
            return anythingButOp(iteration, cpt-1)
        elif char == opening:
            return anythingButClosing(iteration, cpt+1)
        elif char in var:
            return varOrClosing(iteration, cpt)
        else: # char is dot, in op or not in alphabet
            return False
        
    except StopIteration:
        return cpt == 0
        




def varOrClosing(iteration, cpt):
    """
    Take one step in the iterator and search for var or closing.
    
    :param iteration: the string to parse
    :type iteration: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if iteration is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(iteration)
        if cpt == 0:
            return False
        elif char == closing:
            return anythingButOp(iteration, cpt-1)
        elif char in var:
            return onlyClosing(iteration, cpt)
        else: # char is op, dot, opening or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0








def onlyClosing(iteration, cpt):
    """
    Take one step in the iterator and search only for closing.
    
    :param iteration: the string to parse
    :type iteration: iterator
    :param cpt: take count of the opening bracket that are not yet closed
    :type cpt: int
    :return: true if iteration is well formed, false otherwise
    :rtype: bool
    """
    try:
        char = next(iteration)
        if cpt == 0:
            return False
        elif char == closing:
            return anythingButOp(iteration, cpt-1)
        else: # char is opening, in var, op or not in the alphabet
            return False

    except StopIteration:
        return cpt == 0




















if __name__ == '__main__':
    import doctest
    doctest.testmod()
