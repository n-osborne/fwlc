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
import lexpr

def readExp(string):
    """
    Call buildTree on the tranformation of a string into an iterator
    
    :param string: the representation of a lambda expression
    :type string: str
    :return: the tree modeling the lambda expression
    :rtype: dict
    """
    return buildTree(iter(string))
 


def buildTree(iterator):
    """
    Transform a string representing a lambda expression into a binary tree
    modeling this same lambda expression.

    :param iterator: the representation of the lambda expression in an iterator
    :type string: str_iterator
    :return: the tree modeling the lambda expression
    :rtype: dict
    :Examples:


    """
    pass







def buildExpr(tree):
    """
    Build the lambda expression corresponding to the tree.

    :param tree: the tree modeling the lambda expression
    :type tree: dict
    :return: the lambda expression modeled by the tree
    :rtype: dict
    :Examples:


    """
    pass




















if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)