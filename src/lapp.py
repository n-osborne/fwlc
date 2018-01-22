#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lapp
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide modelisation for lambda expressions of the form application.
"""



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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
