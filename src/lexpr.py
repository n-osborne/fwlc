#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lexpr
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a general modelisation for lambda expressions.
"""



class LambdaExpr():
    """
    General class for lambda expressions. 

    :param expression: the lambda expression
    :type expression: LambdaVar, LambdaApp or LambdaAbs

    :attributes:
    - expression

    :methods:
    - __init__(self, expression)
    - __repr__(self)
    - applyTo(self, other : Expression)
    - absractVar(self, var)
    - getContent(self)
    - getFreeVar(self)
    - rename(self)
    - betaReduction(self)
    - etaReduction(self)
    - isBetaNormal(self)
    - isAlphaEq(self, other : Expression)
    - isBetaEq(self, other : Expression)
    - isEtaEq(self, other : Expression)

    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
