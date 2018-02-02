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

 
    def __eq__(self, other):
        """
        This is used for strict equivalence, that is for two lambda expressions
        that are written exactly the same.

        :return:
           - True if self == other
           - False otherwise
        :rtype: bool
        :Examples:

        >>> from lvar import *
        >>> x = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> y = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> z = LambdaApp(LambdaVar("z"), LambdaVar("y"))
        >>> x == y
        True
        >>> x == z
        False
        """
        return self.__repr__() == other.__repr__()





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
        




    def rename(self, old_name, new_name):
        """
        Change all the occurences of old_var to new_var.

        .. note::
           Beware that the choice of a fresh new_var is at the charge of the
           user.

        :param old_name: the name of the variable to rename
        :type old_name: str
        :param new_name: the new name to give
        :type new_name: str
        :UC: new_name in VAR_SET == True
        :Examples:

        >>> from lvar import *
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> xyz = LambdaApp(LambdaApp(LambdaVar("x"), LambdaVar("y")), LambdaVar("z"))
        >>> xy.rename("x", "u")
        >>> xy.function.getName() == "u"
        True
        >>> xyz.rename("y", "o")
        >>> xyz.function.argument.getName() == "o"
        True
        """
        try:
            assert new_name in VAR_SET
            self.function.rename(old_name, new_name)
            self.argument.rename(old_name, new_name)
        except AssertionError:
            raise LambdaAppError("This is not the name of a lambda variable.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
