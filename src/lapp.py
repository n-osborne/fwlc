#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lapp
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018

:synopsis: Provide modelisation for lambda expressions of the form application.
"""

from alphabet_def import *
from lvar import *
from labs import *



class LambdaAppError(Exception):
    """
    Exception for badly formed LambdaApp.
    """
    def __init__(self, msg):
        self.message = msg




class LambdaApp():
    """
    Class for Lambda Application.

    :param function: the expression taken as the function of the application
    :type function: LambdaVar, LambdaApp or LambdaAbs
    :param argument: the expression taken as the argument of the application
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
        """
        try:
            # assert type(function) in {LambdaAbs, LambdaVar, LambdaApp}
            # assert type(argument) in {LambdaAbs, LambdaVar, LambdaApp}
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



    def substitute(self, var_name, expression):
        """
        Substitute the free occurrences of a variable by an expression.
        
        .. note::

           The verification of the fact that the variable is free is done when
           the method is applied to a LambdaAbs.
        
        :param var_name: the variable to substitute
        :type var: str
        :param expression: the expression to put at the place of the variable
        :type expression: LambdaVar, LambdaApp or LambdaAbs
        :return: the new expression with the substitution
        :rtype: LambdaVar, LambdaApp or LambdaAbs
        :UC: var_name is a free occurrence of the variable in the expression
        :Examples:

        >>> from lvar import *
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> np = LambdaApp(LambdaVar("n"), LambdaVar("p"))
        >>> rs = LambdaApp(LambdaVar("r"), LambdaVar("s"))
        >>> newOne = xy.substitute("x", np)
        >>> newOne.function == np # ((np)y)
        True
        >>> newTwo = newOne.substitute("p", rs) # ((n(rs))y)
        >>> newTwo.function.argument == rs
        True
        >>> newThree = newOne.substitute("p", np)
        >>> print(newThree)
        ((n(np))y)
        """
        newFunction = self.function.substitute(var_name, expression)
        newArgument = self.argument.substitute(var_name, expression)
        return LambdaApp(newFunction, newArgument)
        


    def isRedex(self):
        """
        Test whether a Lambda application is a redex or not.

        :return:

           - True if the expression is a redex
           - False otherwise

        :rtype: bool
        :Examples:

        >>> redex = LambdaApp(LambdaAbs("x", LambdaVar("x")), LambdaVar("y"))
        >>> redex.isRedex()
        True
        """
        return type(self.function) == LambdaAbs \
            and (type(self.argument) == LambdaVar\
            or type(self.argument) == LambdaApp\
            or type(self.argument) == LambdaAbs)



    def isBetaNormal(self):
        """
        Test whether a Lambda expression is in its beta normal form.

        :return: 

           - True if the expression is its beta normal form
           - False otherwise

        :rtype: bool
        :Examples:

        >>> redex = LambdaApp(LambdaAbs("x", LambdaVar("x")), LambdaVar("y"))
        >>> redex.isBetaNormal()
        False
        >>> LambdaApp(LambdaVar("x"), LambdaVar("y")).isBetaNormal()
        True
        >>> LambdaApp(LambdaVar("x"), redex).isBetaNormal()
        False
        """
        return (not self.isRedex()) and (self.function.isBetaNormal() and\
                                       self.argument.isBetaNormal())
        


    def betaReduction(self):
        """
        Operate a beta-reduction on the expression.

        :return: the beta-reduct of the expression
        :rtype: LambdaVar, LambdaAbs or LambdaApp
        :UC: the expression must be a redex
        :Examples:

        >>> redex = LambdaApp(LambdaAbs("x", LambdaVar("x")), LambdaVar("y"))
        >>> reduct = redex.betaReduction()
        >>> reduct == LambdaVar("y")
        True
        """
        var_name = self.function.binder
        expression = self.argument
        return self.function.body.substitute(var_name, expression)



    def normalOrderBetaEval(self):
        """
        Operate a beta evaluation according to the normal order.

        .. note::

           According to the normal order, the evaluation begins with the
           leftmost, or the outermost, expression.

        :return: the beta reduct of the expression
        :rtype: LambdaVar, LambdaAbs or LambdaApp
        :Examples:

        """
        # TODO
        pass


    
    def applicativeOrderBetaEval(self):
        """
        Operate a beta evaluation according to the applicative order.

        .. note::
           
           According to the applicative order, the evaluation begins with the
           innermost expression.

        :return: the beta reduct of the expression
        :rtype: LambdaVar, LambdaAbs or LambdaApp
        :Examples:

        """
        # TODO
        pass




if __name__ == '__main__':
    import doctest
    doctest.testmod()
