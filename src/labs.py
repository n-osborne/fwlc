#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: labs
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide a modelisation for lambda expressions of the form abstraction.
"""



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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
