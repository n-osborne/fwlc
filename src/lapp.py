#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lapp
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide modelisation for lambda expressions of the form application.
"""

from alphabet_def import *
import lvar
import labs

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
    :type function: LambdaVar, LambdaApp or LambdaAbs
    :param argument: the lambda expression taken as the argument of the
    application
    :type argument: LambdaVar, LambdaApp or LambdaAbs

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

        >>> from lvar import *
        >>> from labs import *
        >>> x = LambdaVar("x")
        >>> y = LambdaVar("y")
        >>> xy = LambdaApp(x, y)
        >>> type(xy) == LambdaApp
        True
        >>> xyx = LambdaApp(xy, x)
        >>> type(xyx) == LambdaApp
        True
        >>> xz = LambdaApp(x, "z")
        Traceback (most recent call last):
        ...
        LambdaAppError: This is not a lambda application.
        """
        try:
            assert type(function) in {labs.LambdaAbs, lvar.LambdaVar, LambdaApp}
            assert type(argument) in {labs.LambdaAbs, lvar.LambdaVar, LambdaApp}
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
        >>> x = LambdaVar("x")
        >>> y = LambdaVar("y")
        >>> z = LambdaVar("z")
        >>> xy = LambdaApp(x, y)
        >>> print(xy)
        (xy)
        >>> xyz = LambdaApp(xy, z)
        >>> print(xyz)
        ((xy)z)
        """
        return "({}".format(self.function) + "{})".format(self.argument)





    def freeVar(self):
        """
        Get the free variables of the expression.

        :return: the free variables
        :rtype: set
        :Examples:
        
        >>> from lvar import *
        >>> from labs import *
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> xy.freeVar() == {"x", "y"}
        True
        >>> 
        """
        return self.function.freeVar().union(self.argument.freeVar())
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
