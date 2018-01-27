#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: labs
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a modelisation for lambda expressions of the form abstraction.
"""

from alphabet_def import *
import lexpr


class LambdaAbsError(Exception):
    """
    Exception for badly formed LambdaAbs.
    """
    def __init__(self, msg):
        self.message = msg

        



class LambdaAbs():
    """
    Class for Lambda Abstraction.

    :attributes:
    - binder (str)
    - body (lexpr.LambdaExpr)

    :methods:
    - getBody(self)
    - getBinder(self)
    - getFreeVar(self)
    - getBoundVar(self)
    - rename(self, old_var, new_var)
    - substitute(self, var, expression)
    - etaReduct(self)

    """

    def __init__(self, binder, body):
        """
        Constructor for LambdaAbs class.

        :param binder: the binder variable of tha lambda abstraction
        :type binder: str
        :param body: the body of the lambda abstraction
        :type body: lexpr.LambdaExpr
        :UC: binder must be in the alphabet
        :Examples:
        
        >>> import lexpr, lvar
        >>> x = lexpr.LambdaExpr(lvar.LambdaVar("x"))
        >>> identity = LambdaAbs("x", x)
        >>> type(identity) == LambdaAbs
        True
        >>> type(identity.binder) == str
        True
        >>> type(identity.body) == lexpr.LambdaExpr
        True
        >>> binder_error = LambdaAbs(",", x)
        Traceback (most recent call last):
        ...
        LambdaAbsError: This is not a lambda abstraction.
        >>> binder_error = LambdaAbs(x, x)
        Traceback (most recent call last):
        ...
        LambdaAbsError: This is not a lambda abstraction.
        """
        try:
            assert type(binder) == str and\
                binder in VAR_SET and\
                type(body) == lexpr.LambdaExpr
            self.binder = binder
            self.body = body
        except AssertionError:
            raise LambdaAbsError('This is not a lambda abstraction.')

        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
