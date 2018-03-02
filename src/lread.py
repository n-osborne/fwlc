#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lread
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, february

:synopsis: Parser for lambda expressions.

:Tests:

>>> test1 = readExp("(xy)")
>>> type(test1) == dict
True
>>> test1["left"]["root"] == "x"
True
>>> test1["right"]["root"] == "y"
True
>>> exp1 = readTree(test1)
>>> type(exp1) == LambdaExp
True
>>> print(exp1)
(xy)
>>> test2 = readExp("((xy)z)")
>>> type(test2) == dict
True
>>> test2["right"]["root"] == "z"
True
>>> exp2 = readTree(test2)
>>> print(exp2)
((xy)z)
>>> test3 = readExp("((/x.(xy))z)")
>>> type(test3) == dict
True
>>> exp3 = readTree(test3)
>>> print(exp3)
((λx.(xy))z)
"""


import alphabet_def
from lexpr import *
from lapp import *
from labs import *
from lvar import *

import testInput
import testTree

var = alphabet_def.VAR_SET
op = alphabet_def.POSSIBLE_OP
dot = set(alphabet_def.LAMBDA_DOT)
closing = ')'
opening = '('
ignore = dot.union(set(closing))



def read(string):
    """
    Build a LambdaExp according to the string given as argument.

    :param string: the representation of a lambda expression
    :type string: str
    :return: the lambda expression
    :rtype: LambdaExp
    """
    return readTree(readExp(string))



class InputError(Exception):
    """
    Exception class for parsing expression.
    """
    def __init__(self, msg):
        self.message = msg


def readExp(string):
    """
    Check wether the arg is well formed and initialize buildTree.
    
    :param string: the representation of a lambda expression
    :type string: str
    :return: the tree modeling the lambda expression
    :rtype: dict
    """
    if testInput.initParsing(string):
        return buildTree(iter(string))
    else:
        raise InputError("Badly formed string.")
        

 



def buildTree(iterator):
    """
    Transform a string representing a lambda expression into a binary tree
    modeling this same lambda expression.

    :param iterator: the representation of the lambda expression in an iterator
    :type string: str_iterator
    :return: the tree modeling the lambda expression
    :rtype: dict
    :UC: iterator must represent a well formed lambda expression
    :Examples:

    >>> ex1 = buildTree(iter("(bc)"))
    >>> print(ex1["left"])
    {'root': 'b', 'left': None, 'right': None}
    >>> print(ex1["right"])
    {'root': 'c', 'left': None, 'right': None}
    >>> ex2 = buildTree(iter("(f(oo))"))
    >>> print(ex2["left"])
    {'root': 'f', 'left': None, 'right': None}
    """
    try:
        while True:
            char = next(iterator)
            if char in var:
                return {'root': char, 'left': None, 'right': None}
            elif char in op:
                return {'root': char + next(iterator),\
                        'left': None ,'right': None}
            elif char == opening:
                left = buildTree(iterator)
                right = buildTree(iterator)
                return {'root': None, 'left': left, 'right': right}
            else: # char is either dot or closing: do nothing
                pass
    except StopIteration:
        pass


class TreeError(Exception):
    """
    Exception class for parsing tree.
    """
    def __init__(self, msg):
        self.message = msg



def readTree(tree):
    """
    Check wether tree is well formed and initialize buildExpr.

    :param tree: a possible modelisation of a lambda expression
    :type tree: dict
    :return: the corresponding lambda expression
    :rtype: LambdaExp
    """
    if testTree.testTree(tree):
        return LambdaExp(buildExpr(tree))
    else:
        raise TreeError("Tree badly formed.")
 





def buildExpr(tree):
    """
    Build the lambda expression corresponding to the tree.

    :param tree: the tree modeling the lambda expression
    :type tree: dict
    :return: the lambda expression modeled by the tree
    :rtype: dict
    :UC:

       - tree has exactly these three fields: 'root', 'left', 'right'
       - either 'root' is None and the two others are not and contain either a
         tree or a variable or the concatenation of the lambda operator and a
         variable
       - or 'root' is not None but the two other are and the 'root' contains
         either a variable or the concatenation of the lambda operator and a
         variable

    :Examples:

    >>> left1 = {'root': 'x', 'left': None, 'right': None}
    >>> right1 = {'root': 'y', 'left': None, 'right': None}
    >>> ex1 = buildExpr({'root': None, 'left': left1, 'right': right1})
    >>> print(ex1)
    (xy)
    >>> left2 = {'root': '/x', 'left': None, 'right': None}
    >>> right2 = {'root': 'x', 'left': None, 'right': None}
    >>> ex2 = buildExpr({'root': None, 'left': left2, 'right': right2})
    >>> print(ex2)
    (λx.x)
    """
    if tree['root'] in var:
        return LambdaVar(tree['root'])
    elif tree['left']['root'] != None and tree['left']['root'][0] in op:
        return LambdaAbs(tree['left']['root'][1], buildExpr(tree['right']))
    else: # node is None, dict, dict neither contains op
        return LambdaApp(buildExpr(tree['left']),\
                         buildExpr(tree['right']))








if __name__ == '__main__':
    import doctest
    doctest.testmod()
