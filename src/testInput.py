#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: testInput.py
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018; febuary

:synopsis: test weihter a string is a well formed candidate for lread.buildTree
Finite State Machine with four states.

:Tests:

>>> initParsing("(xy)")
True
>>> initParsing("(/x.(xy)(x(ud)))")
True
>>> initParsing("((/r.r)z)")
True
>>> initParsing("((zy)((xy)e))")
True
>>> initParsing("()")
False
>>> initParsing("(Xy)")
False
>>> intiParsing("((xy)z")
False
>>> initParsing("(xy)z)")
False
>>> initParsing("(xyz)")
False
>>> intiParsing("(/x(xy))")
False
"""










if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
