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
>>> test1["root"] == None
True
>>> test1["left"] == "x"
True
>>> test1["right"] == "y"
True
>>> test2 = readExp("(/x.(xy))")
>>> type(test2) == dict
True
>>> test2["root"] == None
True
>>> test2["left"] == "/x"
True
>>> type(test2["right") == dict
True
>>> test3 = readExp("((xy)z)")
>>> type(test3) == dict
True
>>> test3["root"] == None
True
>>> type(test3["left"]) == dict
True
>>> test3["right"] == "z"
True
>>> test3["left"]["root"] == None
True
>>> test3["left"]["left"] == "x"
True
>>> test3["left"]["right"] == "y"
True
>>> test4 = buildExp(test1)
>>> type(test4) == lepxr.LambdaExp
True
>>> print(test4)
(xy)
>>> test5 = buildExp(test2)
>>> print(test5)
(λx.(xy))
>>> test6 = buildExp(test3)
>>> print(test6)
((xy)z)
"""


import alphabet_def
from lexpr import *
from lapp import *
from labs import *
from lvar import *

import testInput
import testTree



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
    try:
        assert testInput.initParsing(string)
        return buildTree(iter(string))
    except AssertionError:
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

    >>> ex1 = buildTree(iter("(bc)")
    >>> print(ex1)
    {'root': None, 'left': 'b', 'right': 'c'}
    >>> ex2 = buildTree(iter("(f(oo))")
    >>> print(ex2)
    {'root': None, 'left': 'f', 'right': {'root': None, 'right': 'o', 'left': 'o'}}
    """
    pass



def readTree(tree):
    """
    Check wether tree is well formed and initialize buildExpr.

    :param tree: a possible modelisation of a lambda expression
    :type tree: dict
    :return: the corresponding lambda expression
    :rtype: LambdaExp
    """
    try:
        # TODO funciton to test input for buildExpr
        assert testTree.testTree(tree)
        return buildExpr(tree)
    except AssertionError:
        pass # TODO define a pretty exception
 





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

    >>> ex1 = buildExpr({'root': None, 'left': 'x', 'right': 'y'})
    >>> print(ex1)
    (xy)
    >>> ex2 = buildEpxr({'root': None, 'left': '/x', 'right': 'x'})
    >>> print(ex2)
    (λx.x)
    """
    pass








if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
