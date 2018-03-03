#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: testTree.py
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date:

:synopsis: test wether a tree modeling a lambda expression is correctly formed.

:Tests:

>>> tree1 = {'root': 'x', 'left': None, 'right': None}
>>> testTree(tree1)
True
>>> tree2 = {'root': None, 'left': tree1, 'right': tree1}
>>> testTree(tree2)
True
>>> tree3 = {'root': '/x', 'left': None, 'right': None}
>>> testTree(tree3)
True
>>> testTree({'root': None, 'left': tree3, 'right': tree2})
True
>>> testTree({'root': None, 'left': tree1})
False
>>> testTree({'root': None, 'right': tree3, 'right': tree2, 'bud': tree1})
False
>>> testTree({'root': 'x', 'left': 'y', 'right': None})
False
>>> testTree({'root': None, 'left': 'x', 'rigth': 'y'})
False
"""


import lib.alphabet_def

var = lib.alphabet_def.VAR_SET
op = lib.alphabet_def.POSSIBLE_OP


def testTree(tree):
    """
    Test wether tree is a well formed input for buildExpr.

    :param tree: a candidate for buildExpr
    :type tree: dict
    :return: True if tree is a well formed input for buildExpr, false otherwise
    :rtype: bool
    """
    try:
        assert type(tree) == dict
        assert tree.keys() == {'root', 'left', 'right'}
        
        if tree['root'] == None:
            return testTree(tree['left']) and testTree(tree['right'])
        elif tree['root'] in var:
            return tree['left'] == None and tree['right'] == None
        elif len(tree['root']) == 2\
             and tree['root'][0] in op\
             and tree['root'][1] in var:
            return tree['left'] == None and tree['right'] == None
        else:
            return False

    except AssertionError:
        return False




















if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
