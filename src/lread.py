#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lread
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, february

:synopsis: Parser for lambda expressions.
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
