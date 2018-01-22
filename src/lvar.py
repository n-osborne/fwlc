#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lvar
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide modelisation for lambda expressions of the form simple name.
"""



class LambdaVar():
    """
    Class for Lambda Variable.

    :param name: the name of the variable
    :type name: str
    :UC: the name must be in the alphabet

    :attributes:
    - name

    :methods:
    - __init__(self, name)
    - __repr__(self)
    - getName(self)
    - rename(self)
    - getFreeVar(self)
    - 

    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
