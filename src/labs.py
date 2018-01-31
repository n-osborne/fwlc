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
        :type body: LambdaVar, LambdaApp or LambdaAbs
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
        
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
