#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:module name: lvar
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, January

:synopsis: Provide modelisation for lambda expressions of the form simple name.
"""

from alphabet_def import *


class LambdaVarError(Exception):
    """
    Exception for badly formed LambdaVar.
    """
    def __init__(self, msg):
        self.message = msg




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
    - rename(self, newName)
    - substitute(self, var_name, expression)
    - getFreeVar(self)
    - isBetaNormal(self)
    """



    def __init__(self, name):
        """
        Constructor for LambdaVar class.

        :param name: the name of the variable
        :type name: str
        :UC: name must be in the alphabet of variable
        :Examples:

        >>> x = LambdaVar("x")
        >>> print(x.name)
        x
        >>> type(x) == LambdaVar
        True
        >>> type(x.name) == str
        True
        >>> error = LambdaVar(3)
        Traceback (most recent call last):
        ...
        LambdaVarError: This is not a lambda variable.
        """
        try:
            assert name in VAR_SET
            self.name = name
        except AssertionError:
            raise LambdaVarError('This is not a lambda variable.')



    def __repr__(self):
        """
        Provide a readable representation of LambdaVar.
        :Examples:

        >>> x = LambdaVar("x")
        >>> print(x)
        x
        """
        return self.name



    def __eq__(self, other):
        """
        This is used for strict equivalence, that is for two lambda expressions
        that are written exactly the same.

        :return:

           - True if self == other
           - False otherwise

        :rtype: bool
        :Examples:

        >>> x1 = LambdaVar("x")
        >>> x2 = LambdaVar("x")
        >>> y = LambdaVar("y")
        >>> x1 == x2
        True
        >>> x1 == y
        False
        """
        return self.__repr__() == other.__repr__()



    def getName(self):
        """
        Get the name of the variable.
        
        >>> LambdaVar("x").getName() == "x"
        True
        """
        return self.name



    def rename(self, old_name, new_name):
        """
        Rename the variable.

        :param old_name: the name of the variable to rename
        :type old_name: str
        :param new_name: the new name to give
        :type new_name: str
        :UC: new_name in VAR_SET == True
        :Examples:

        >>> x = LambdaVar("x")
        >>> x.rename("x", "y")
        >>> x.getName() == "y"
        True
        >>> x.rename("x", "z")
        >>> x.getName() == "z"
        False
        >>> x.getName() == "y"
        True
        >>> x.rename("y", "?")
        Traceback (most recent call last):
        ...
        LambdaVarError: This is not the name of a lambda variable.
        """
        try:
            assert new_name in VAR_SET
            if self.name == old_name:
                self.name = new_name
        except AssertionError:
            raise LambdaVarError("This is not the name of a lambda variable.")



    def freeVar(self):
        """
        Get free variable in the expression.

        :return: the name of the variable
        :rtype: str
        :Examples:

        >>> x = LambdaVar("x")
        >>> x.freeVar() == {"x"}
        True
        """
        return set(self.name)



    def substitute(self, var_name, expression):
        """
        Substitute a variable by the given expression.
        
        :param var_name: the name of the variable to be substituted
        :type var_name: str
        :param expression: the expression to substitute to the variable
        :type expression: LambdaVar, LambdaApp or LambdaAbs
        :return: the new expression
        :rtype: LambdaVar, LambdaApp or LambdaAbs
        :Examples:

        >>> from lapp import *
        >>> x = LambdaVar("x")
        >>> yz = LambdaApp(LambdaVar("y"), LambdaVar("z"))
        >>> newOne = x.substitute("x", yz)
        >>> newOne == yz
        True
        >>> newTwo = x.substitute("y", yz)
        >>> newTwo == x
        True
        """
        if self.getName() == var_name:
            return expression
        else:
            return self



    def isRedex(self):
        """
        Fill the contract for Beta evaluation.
            
        :return: false
        :rtype: boolean
        """
        return false



    def isBetaNormal(self):
        """
        Test whether a Lambda expression is in its beta normal form.

        :return: 

           - True if the expression is its beta normal form
           - False otherwise

        :rtype: bool
        :Examples:

        >>> LambdaVar("x").isBetaNormal()
        True
        """
        return True



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
