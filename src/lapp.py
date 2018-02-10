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



    def oneStepNOBetaEval(self):
        """
        Perform one step of a normal order Beta-evaluation.

        .. note::

           According to the normal order, the evaluation begins with the
           leftmost, or the outermost, expression.

           If expression is not a redex, choice is made here to evaluate from
           the right to the left (function then argument)
 
        :return: he one step Beta-evaluation of the expression.
        :rtype: LambdaAbs, LambdaApp or LambdaVar
        :UC: Expression must not be in beta normal form
        :Examples:


        >>> # First test - step by step beta evaluation
        ... abs1 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> redex1 = LambdaApp(abs1, LambdaApp(LambdaVar("z"), LambdaVar("t")))
        >>> rs = LambdaApp(LambdaVar("r"), LambdaVar("s"))
        >>> expr1 = LambdaApp(LambdaAbs("z", redex1), rs)
        >>> print(expr1)
        ((λz.((λx.(xy))(zt)))(rs))
        >>> result1_1 = expr1.oneStepNOBetaEval()
        >>> print(result1_1)
        ((λx.(xy))((rs)t))
        >>> result1_2 = result1_1.oneStepNOBetaEval()
        >>> print(result1_2)
        (((rs)t)y)
        >>> # Second test - step by step beta evaluation
        ... abs2 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> abs3 = LambdaAbs("z", LambdaApp(LambdaVar("z"), LambdaVar("z")))
        >>> redex2 = LambdaApp(abs3, LambdaVar("t"))
        >>> expr2 = LambdaApp(abs2, redex2)
        >>> print(expr2)
        ((λx.(xy))((λz.(zz))t))
        >>> result2_1 = expr2.oneStepNOBetaEval()
        >>> print(result2_1)
        (((λz.(zz))t)y)
        >>> result2_2 = result2_1.oneStepNOBetaEval()
        >>> print(result2_2)
        ((tt)y)
        >>> # Third test - step by step beta evaluation
        ... double = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("x")))
        >>> applyTo_t = LambdaAbs("z", LambdaApp(LambdaVar("t"), LambdaVar("z")))
        >>> future_tr = LambdaApp(applyTo_t, LambdaVar("r"))
        >>> expr3 = LambdaApp(double, future_tr)
        >>> print(expr3)
        ((λx.(xx))((λz.(tz))r))
        >>> result3_1 = expr3.oneStepNOBetaEval()
        >>> print(result3_1)
        (((λz.(tz))r)((λz.(tz))r))
        >>> result3_2 = result3_1.oneStepNOBetaEval()
        >>> print(result3_2)
        ((tr)((λz.(tz))r))
        >>> result3_3 = result3_2.oneStepNOBetaEval()
        >>> print(result3_3)
        ((tr)(tr))
        """
        # TODO exception handling
        if self.isRedex():
            return self.betaReduction()
        elif not self.function.isBetaNormal():
            return LambdaApp(self.function.oneStepNOBetaEval(),\
                             self.argument)
        else:
            return LambdaApp(self.function,\
                             self.argument.oneStepNOBetaEval())



    def oneStepAOBetaEval(self):
        """
        Perform one step of beta evaluation in applicative order.

        .. note::
           
           According to the applicative order, the evaluation begins with the
           innermost expression.
        
           Here, the choice is made to begin with the argument of the Lambda
           Application, that is from the right to the left.

        :return: the one step Beta-evaluation of the expression
        :rtype: LambdaVar, LambdaAbs or LambdaApp
        :UC: self must not be in its beta normal form
        :Examples:
 
        >>> # First test - step by step beta evaluation
        ... abs1 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> redex1 = LambdaApp(abs1, LambdaApp(LambdaVar("z"), LambdaVar("t")))
        >>> rs = LambdaApp(LambdaVar("r"), LambdaVar("s"))
        >>> expr1 = LambdaApp(LambdaAbs("z", redex1), rs)
        >>> print(expr1)
        ((λz.((λx.(xy))(zt)))(rs))
        >>> result1_1 = expr1.oneStepAOBetaEval()
        >>> print(result1_1)
        ((λz.((zt)y))(rs))
        >>> result1_2 = result1_1.oneStepAOBetaEval()
        >>> print(result1_2)
        (((rs)t)y)
        >>> # Second test - step by step beta evaluation
        ... abs2 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
        >>> abs3 = LambdaAbs("z", LambdaApp(LambdaVar("z"), LambdaVar("z")))
        >>> redex2 = LambdaApp(abs3, LambdaVar("t"))
        >>> expr2 = LambdaApp(abs2, redex2)
        >>> print(expr2)
        ((λx.(xy))((λz.(zz))t))
        >>> result2_1 = expr2.oneStepAOBetaEval()
        >>> print(result2_1)
        ((λx.(xy))(tt))
        >>> result2_2 = result2_1.oneStepAOBetaEval()
        >>> print(result2_2)
        ((tt)y)
        >>> # Third test - step by step beta evaluation
        ... double = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("x")))
        >>> applyTo_t = LambdaAbs("z", LambdaApp(LambdaVar("t"), LambdaVar("z")))
        >>> future_tr = LambdaApp(applyTo_t, LambdaVar("r"))
        >>> expr3 = LambdaApp(double, future_tr)
        >>> print(expr3)
        ((λx.(xx))((λz.(tz))r))
        >>> result3_1 = expr3.oneStepAOBetaEval()
        >>> print(result3_1)
        ((λx.(xx))(tr))
        >>> result3_2 = result3_1.oneStepAOBetaEval()
        >>> print(result3_2)
        ((tr)(tr))
        """    
        # TODO exception handling
        if not self.argument.isBetaNormal():
            return LambdaApp(self.function,\
                             self.argument.oneStepAOBetaEval())
        elif not self.function.isBetaNormal():
            return LambdaApp(self.function.oneStepAOBetaEval(),\
                             self.argument)
        else:
            return self.betaReduction()

        

    # def normalOrderBetaEval(self):
    #     """
    #     Operate a beta evaluation according to the normal order.

    #     .. note::

    #        According to the normal order, the evaluation begins with the
    #        leftmost, or the outermost, expression.

    #        If expression is not a redex, choice is made here to evaluate from
    #        the right to the left (function then argument)
    
    #     :return: all the steps of the beta evaluation
    #     :rtype: list of LambdaVar, LambdaAbs or LambdaApp
    #     :UC: lambda expression must have been renamed according to the
    #     Barenbergt convention.
    #     :Examples:

    #     >>> # First test
    #     ... abs1 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
    #     >>> redex1 = LambdaApp(abs1, LambdaApp(LambdaVar("z"), LamdaVar("t")))
    #     >>> rs = LambdaApp(LambdaVar("r"), LamdaVar("s"))
    #     >>> expr1 = LambdaApp(LambdaAbs("z", redex1), rs)
    #     >>> result1 = normalOrderBetaEval(expr1)
    #     >>> print(result1)
    #     [((λz.((λx.(xy))(zt)))(rs)), ((λx.(xy))((rs)t)), (((rs)t)y), (((rs)t)y)]
    #     >>> # Second test
    #     ... abs2 = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("y")))
    #     >>> abs3 = LambdaAbs("z", LambdaApp(LambdaVar("z"), LambdaVar("z")))
    #     >>> redex2 = LambdaApp(abs3, LambdaVar("t"))
    #     >>> expr2 = LambdaApp(abs2, redex2)
    #     >>> result2 = normalOrderBetaEval(expr2)
    #     >>> print(result2)
    #     [((λx.(xy))((λz.(zz))t)), (((λz.(zz))t)y), ((tt)y)]
    #     >>> # Third test
    #     ... double = LambdaAbs("x", LambdaApp(LambdaVar("x"), LambdaVar("x")))
    #     >>> applyTo_t = LambdaAbs("z", LambdaApp(LambdaVar("t"), LambdaVar("z")))
    #     >>> future_tr = LambdaApp(applyTo_t, LambdaVar("r"))
    #     >>> expr3 = LambdaApp(double, future_tr)
    #     >>> result3 = normalOrderBetaEval(expr3)
    #     >>> print(result3)
    #     [((λx.(xx))((λz.(tz))r)), (((λz.(tz))r)((λz.(tz))r)), ((tr)((λz.(tz))r)), ((tr)(tr))]
    #     """
    #     # TODO
    #     pass


    
    # def applicativeOrderBetaEval(self):
    #     """
    #     Operate a beta evaluation according to the applicative order.

    #     .. note::
           
    #        According to the applicative order, the evaluation begins with the
    #        innermost expression.

    #     :return: the beta reduct of the expression
    #     :rtype: LambdaVar, LambdaAbs or LambdaApp
    #     :Examples:

    #     """
    #     # TODO
    #     pass




if __name__ == '__main__':
    import doctest
    doctest.testmod()
