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




def buildTree(string, index):
    """
    Transform a string representing a lambda expression into a binary tree
    modeling this same lambda expression.

    :param string: the representation of the lambda expression
    :type string: str
    :param index: an index to keep track of the parsing
    :type index: int
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
