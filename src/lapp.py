#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lapp
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide modelisation for lambda expressions of the form application.
"""

from alphabet_def import *
from lexpr import *

class LambdaAppError(Exception):
    """
    Exception for badly formed LambdaApp.
    """
    def __init__(self, msg):
        self.message = msg

class LambdaApp():
    """
    Class for Lambda Application.

    :param function: the lambda expression taken as the function of the
    application
    :type function: lexpr.LambdaExpr
    :param argument: the lambda expression taken as the argument of the
    application
    :type argument: lexpr.LambdaExpr

    :attributes:
    - function
    - argument

    :methods:
    - __initi__
    - __repr__
    - getFunction(self)
    - getArgument(self)
    - getFreeVar(self)
    - getBoundVar(self)
    - rename(self, old_var, new_var)
    - substitute(self, var, expression)
    - betaReduct(self)

    """


    def __init__(self, function, argument):
        """
        Constructor for LambdaApp class.

        :param function: the function of the lambda application
        :type function: lexpr.LambdaExpr
        :param argument: the argument passed to the function of the lambda application
        :type argument: lexpr.LambdaExpr
        :Examples:

        >>> import lexpr, lvar
        >>> x = lexpr.LambdaExpr(lvar.LambdaVar("x"))
        >>> y = lexpr.LambdaExpr(lvar.LambdaVar("y"))
        >>> xy = LambdaApp(x, y)
        >>> type(xy) == LambdaApp
        True
        >>> type(xy.function) == lexpr.LambdaExpr
        True
        >>> type(xy.argument) == lexpr.LambdaExpr
        True
        >>> xz = LambdaApp(x, lvar.LambdaVar("z"))
        Traceback (most recent call last):
        ...
        LambdaAppError: This is not a lambda application.
        """
        try:
            assert type(function) == lexpr.LambdaExpr\
                and type(argument) == lexpr.LambdaExpr
            self.function = function
            self.argument = argument
        except AssertionError:
            raise LambdaAppError('This is not a lambda application.')

    def __repr__(self):
        """
        Provide a readable representaition for LambdaApp.

        :Examples:
    
        >>> from lexpr import *
        >>> from lvar import *
        >>> x = LambdaExpr(LambdaVar("x"))
        >>> y = LambdaExpr(LambdaVar("y"))
        >>> z = LambdaExpr(LambdaVar("z"))
        >>> xy = LambdaApp(x, y)
        >>> print(xy)
        (xy)
        >>> xyz = LambdaApp(LambdaExpr(xy), z)
        >>> print(xyz)
        ((xy)z)
        """
        return "({}".format(self.function.expression) + "{})".format(self.argument.expression)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
