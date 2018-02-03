#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: labs
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a modelisation for lambda expressions of the form abstraction.
"""

from alphabet_def import *
import lvar
import lapp


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
    - body (LambdaVar, LambdaApp or LambdaAbs)

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
        :type body: 
        
           - LambdaVar 
           - LambdaApp
           - LambdaAbs

        :UC: binder must be in the alphabet
        :Examples:
        
        >>> from lvar import *
        >>> from lapp import *
        >>> x = LambdaVar("x")
        >>> identity = LambdaAbs("x", x)
        >>> type(identity) == LambdaAbs
        True
        >>> type(identity.binder) == str
        True
        >>> type(identity.body) in {LambdaAbs, LambdaVar, LambdaApp}
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
            assert type(binder) == str
            assert binder in VAR_SET
            assert type(body) in {LambdaAbs, lvar.LambdaVar, lapp.LambdaApp}
            self.binder = binder
            self.body = body
        except AssertionError:
            raise LambdaAbsError('This is not a lambda abstraction.')

        
    def __repr__(self):
        """
        Provide readable representation for LambdaAbs
        :Examples:

        >>> from lexpr import *
        >>> from lvar import *
        >>> from lapp import *
        >>> x = LambdaVar("x")
        >>> identity = LambdaAbs("x", x)
        >>> print(identity)
        (λx.x)
        >>> false = LambdaAbs("y", identity)
        >>> print(false)
        (λy.(λx.x))
        >>> double = LambdaAbs("x", LambdaApp(x, x))
        >>> print(double)
        (λx.(xx))
        """
        rep = "({}".format(LAMBDA_OP)
        rep += self.binder
        rep += LAMBDA_DOT
        rep += "{}".format(self.body)
        rep += ")"
        return rep
        
 
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
        >>> x = LambdaAbs("x", LambdaVar("x"))
        >>> y = LambdaAbs("x", LambdaVar("x"))
        >>> z = LambdaAbs("z", LambdaVar("x"))
        >>> x == y
        True
        >>> x == z
        False
        """
        return self.__repr__() == other.__repr__()

       

    def freeVar(self):
        """
        Get free variables in the expression.

        :return: the name of the free variables
        :rtype: str
        :Examples:

        >>> from lvar import *
        >>> from lapp import *
        >>> LambdaAbs("x", LambdaVar("x")).freeVar() == set()
        True
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> LambdaAbs("x", xy).freeVar() == {"y"}
        True
        """
        return self.body.freeVar() - set(self.binder)

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
        >>> from lapp import *
        >>> identity = LambdaAbs("x", LambdaVar("x"))
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> apply_y = LambdaAbs("x", xy)
        >>> identity.rename("x", "y")
        >>> identity.binder == "y"
        True
        >>> identity.body.getName() == "y"
        True
        >>> apply_y.rename("y", "l")
        >>> apply_y.freeVar() == {"l"}
        True
        """
        try:
            assert new_name in VAR_SET
            if self.binder == old_name:
                self.binder = new_name
            self.body.rename(old_name, new_name)
        except AssertionError:
            raise LambdaAbsError("This is not the name of a lambda variable.")



    def substitute(self, var, expression):
        """
        Substitute the free occurrences of a variable by an expression.
        
        .. note::

           The verification of the fact that the variable is free is done when
           the method is applied to a LambdaAbs.

        :param var: the variable to substitute
        :type var: str
        :param expression: the expression to put at the place of the variable
        :type expression: 

           - LambdaVar
           - LambdaApp
           - LambdaAbs

        :UC: var is a free occurrence of the variable in the expression
        :Examples:

        >>> from lvar import *
        >>> from lapp import *
        >>> xy = LambdaApp(LambdaVar("x"), LambdaVar("y"))
        >>> np = LambdaApp(LambdaVar("n"), LambdaVar("p"))
        >>> abstraction = LambdaAbs("x", xy)
        >>> abstraction.substitute("x", np)
        >>> abstraction.body == xy
        True
        >>> abstraction.substitute("y", np)
        >>> abstraction.body.argument == np
        True
        """
        if self.binder != var:
            # perhaps a silly test?
            # the case is: /x.y which is legal but idiotic
            if self.body == var:
                self.body = expression
            else:
                self.body.substitute(var, expression)




        

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
