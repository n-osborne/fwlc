.. fwlc documentation master file, created by
   sphinx-quickstart on Sat Jan 20 18:34:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to fwlc's documentation!
================================

Fun with λ-calculus (fwlc for short) is an evaluator and explorator for Lambda
Calculus.

As an interpretor, fwlc can evaluate lambda expression, that is:

- perform β-reduction.
- perform η-reduction.

As an explorator, fwlc is able to give the user some meta-informations about a
lambda expression. Here is a short list of the possibilities:

- test whether a lambda expression is in its β-normal form.
- give the set of free variables in a given lambda expression.
- test for the β-equivalence of two given lambda expressions. 
- test for the α-equivalence of two given lambda expressions. 

In order, for the user to interact with fwlc, it offers a prompt in a terminal.
Lambda expressions are represented in a way that is readable for the user and
the machine. The choice of the author are:

- none of the parentheses are omitted except around a simple variable.
- the lambda operator is represented by the greek letter 'λ' but the user can
  use the character '/' to facilitate the input.

Here are some examples:

============ ======================= =========
Expression   Representation          Input
============ ======================= =========
Variable     :math:`x`                x
Application  :math:`(xy)`             (xy)
Application  :math:`((xy)z)`          ((xy)z)
Application  :math:`(x(yz))`          (x(yz))
Abstraction  :math:`(\lambda x.(x))`  (/x.(x))
============ ======================= =========
   
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   lvar
   lapp
   labs
   lexpr




   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
