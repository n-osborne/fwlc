#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lexpr
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a general modelisation for lambda expressions.
"""

from alphabet_def import *


class LambdaExprError(Exception):
    """
    Exception for badly formed LambdaExpr.
    """
    def __init__(self, msg):
        self.message = msg



        
class LambdaExpr():
    """
    General class for lambda expressions. 

    :param expression: the lambda expression
    :type expression: LambdaVar, LambdaApp or LambdaAbs

    :attributes:
    - expression

    :methods:
    - __init__(self, expression : LambdaVar, LambdaApp or LambdaAbs)
    - __repr__(self)
    - applyTo(self, other : Expression)
    - absractVar(self, var : str)
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

    def __init__(self, expression):
        """
        Constructor for LambdaExpr class.

        :param expression: the lambda expression contained in the object
        :type expression: LambdaVar, LambdaApp or LambdaAbs
        
        """
        try:
            assert type(expression) in (lvar.LambdaVar, lapp.LambdaApp, labs.LambdaAbs)
            self.expression = expression
        except AssertionError:
            raise LambdaExprError("This is not a lambda expression.")
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
