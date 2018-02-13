#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lexpr
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, February

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



    def applyTo(self, other):
        """
        Build a Lambda application from two Lambda expressions.

        :param other: the Lambda expression to which we apply the actual one
        :type other: LambdaExp
        :return: the application of the expression to the other
        :rtype: LambdaExp
        :Examples:

        >>> arg = LambdaExp(LambdaVar("y"))
        >>> fun = LambdaExp(LambdaVar("x"))
        >>> new = arg.applyTo(fun)
        >>> print(new)
        (xy)
        """
        arg = self.expression
        fun = other.expression
        return LambdaExp(LambdaApp(fun, arg))
        
        

    def abstractVar(self, var):
        """
        Build a lambda abstraction from the expression with the given variable.

        :param var: the binder of the returned abstraction
        :type var: str
        :return: the lambda abstraction composed of var as binder and the
        expression as body
        :rtype: LambdaExp
        :Examples:

        >>> arg = LambdaExp(LambdaVar("y"))
        >>> fun = LambdaExp(LambdaVar("x"))
        >>> expr = LambdaExp(LambdaApp(arg, fun))
        >>> abs = expr.abstractVar("x")
        >>> type(abs.expression) == LambdaAbs
        True
        >>> abs.expression.binder == "x"
        True
        >>> abs.expression.body == expr.expression
        True
        """
        return LambdaExp(LambdaAbs(var, self.expression))



    def betaEvalWithTraces(self, evalMode="normal"):
        """
        Perform a complete beta evaluation.
        
        :param evalMode: order of evaluation, either normal (default) or applicative
        :type evalMode: str
        :return: the list of all the steps
        :rtype: list
        :Examples:
        
        >>> # First test - normal order
        ... double = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("x")))
        >>> applyTo_t = LambdaAbs("z", LambdaApp(LambdaVar("t"), LambdaVar("z")))
        >>> future_tr = LambdaApp(applyTo_t, LambdaVar("r"))
        >>> expr = LambdaExp(LambdaApp(double, future_tr))
        >>> print(expr)
        ((λx.(xx))((λz.(tz))r))
        >>> result_1 = expr.betaEvalWithTraces()
        >>> print(result_1)
        [((λx.(xx))((λz.(tz))r)), (((λz.(tz))r)((λz.(tz))r)), ((tr)((λz.(tz))r)), ((tr)(tr))]
        >>> # Second test - applicative order
        ... result_2 = expr.betaEvalWithTraces("applicative")
        >>> print(result_2)
        [((λx.(xx))((λz.(tz))r)), ((λx.(xx))(tr)), ((tr)(tr))]
        """
        # DONE: docstring
        # DONE: doctests
        # DONE: function avoiding name clash in betaReduction - TODO: to test
        # DONE: implementation
        trace = [self]
        expr = self.expression
        if evalMode == "normal":
            while not expr.isBetaNormal():
                expr = expr.oneStepNOBetaEval()
                trace.append(LambdaExp(expr))
            return trace
        elif evalMode == "applicative":
            while not expr.isBetaNormal():
                expr = expr.oneStepAOBetaEval()
                trace.append(LambdaExp(expr))
            return trace





if __name__ == '__main__':
    import doctest
    doctest.testmod()
