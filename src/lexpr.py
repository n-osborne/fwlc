#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lexpr
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a general modelisation for lambda expressions.
"""

from alphabet_def import *
from lvar import *
from lapp import *
from labs import *

class LambdaExpError(Exception):
    """
    Exception for badly formed LambdaExp.
    """
    def __init__(self, msg):
        self.message = msg



        
class LambdaExp():
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
        :type expression:
        
           - LambdaVar
           - LambdaApp
           - LambdaAbs

        :Examples:

        >>> from lvar import *
        >>> x = LambdaExp(LambdaVar("x"))
        >>> type(x) == LambdaExp
        True
        >>> type(x.expression) == LambdaVar
        True
        >>> error = LambdaExp(x)
        Traceback (most recent call last):
        ...
        LambdaExpError: This is not a lambda expression.
        
        """
        try:
            assert type(expression) in (LambdaVar, LambdaApp,\
                                        LambdaAbs)
            self.expression = expression
        except AssertionError:
            raise LambdaExpError("This is not a lambda expression.")


        
    def __repr__(self):
        """
        Provide readable representation for LambdaExp.
        :Examples:

        >>> from lvar import *
        >>> from lapp import *
        >>> from labs import *
        >>> x = LambdaExp(LambdaVar("x"))
        >>> print(x)
        x
        >>> xy = LambdaExp(LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> print(xy)
        (xy)
        """
        return "{}".format(self.expression)
 


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
        >>> from lapp import *
        >>> x = LambdaExp(LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> y = LambdaExp(LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> z = LambdaExp(LambdaApp(LambdaVar("z"), LambdaVar("y")))
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
        >>> from lapp import *
        >>> from labs import *
        >>> x = LambdaVar("x")
        >>> LambdaExp(x).freeVar() == {"x"}
        True
        >>> LambdaExp(LambdaApp(x, x)).freeVar() == {"x"}
        True
        >>> y = LambdaVar("y")
        >>> xy = LambdaApp(x, y)
        >>> LambdaExp(xy).freeVar() == {"x", "y"}
        True
        >>> LambdaExp(LambdaAbs("x", xy)).freeVar() == {"y"}
        True
        >>> LambdaExp(LambdaAbs("y", xy)).freeVar() == {"x"}
        True
        """
        return self.expression.freeVar()
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
