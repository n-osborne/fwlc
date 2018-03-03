#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:program name: fwlc
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, Mars

:synopsis: REPL for Fun With Lambda Calculus
"""

import lib.lexpr
import lib.lread
from string import ascii_uppercase

PROMPT = "<°λ°> " 
DIC = dict()


def repl_loop():
    """
    REPL loop for fwlc.
    """
    while True:
        
        command = input(PROMPT).split()

        # general commands
        
        if command[0] == ":q" or command == ":quit":
            print("Goodbye!")
            break

        elif (command[0] in (":h", ":help")) and len(command) == 1:
            printHelp() # TODO complete function printHelp

        elif command[0] == ':license':
            with open("LICENSE", "r") as stream :
                print(stream.read())
                
        elif command[0][0] != ":" and len(command) == 3 and command[1] == "=":
            try:
                assert set(command[0]).issubset(ascii_uppercase)
                DIC[command[0]] = lib.lread.read(command[2])
            except AssertionError:
                print("This is not a valid identificator.")
            except:
                print("That does not seem to be a correct lambda expression.")

        elif command[0] in DIC.keys():
            print(DIC[command[0]])

        elif command[0] == ":NOBeval":
            try:
                assert command[1] in DIC.keys()
                traces = DIC[command[1]].betaEvalWithTraces()
                for exp in traces:
                    print(exp)
            except AssertionError:
                print("That is not a valid identificator.")

        elif command[0] == ":AOBeval":
            try:
                assert command[1] in DIC.keys()
                traces = DIC[command[1]].betaEvalWithTraces(applicative)
                for exp in traces:
                    print(exp)
            except AssertionError:
                print("That is not a valid identificator.")
               
        elif command[0] == ":info":
            try:
                assert command[1] in DIC.keys()
                exp = DIC[command[1]]
                print(exp)
                if exp.isBetaNormal():
                    print("Lambda expression in its Beta normal form.")
                else:
                    print("Lambda expression that can be beta evaluated.")
                FV = exp.freeVar()  
                if FV == set():
                    print("This is a combinator.")
                else:
                    print("This is the set of free variables:")
                    print(FV)

            except AssertionError:
                print("This is not a valid identificator.")



def greeting():
    """
    Print greeting message for repl loop of fwlc.
    """
    print("Greeting.")
    print("Welcome in  Fun With λ Calculus.")
    print()
    print("Type :h or :help for help.")
    print()
    


def printHelp():
    """
    Print the help of the REPL for Fun With Lambda Calculus.
    """
    print()
    print("\tDON'T PANIC!")
    print()
    print("\tList of commands:")
    print("\t-----------------")
    print("\t :h or :help :: print this help.")
    print("\t :q or :quit :: exit the RELP.")
    print("\t :NOBeval <Id> :: print all the steps of a Beta-evaluation\n\t\t\
    in normal order of the lambda expression attached to the Id")
    print("\t :AOBeval <Id> :: print all the steps of a Beta-evaluation\n\t\t\
    in applicative order of the lambda expression attached to the Id")
    print("\t :info <Id> :: print some info about the lambda expression\n\t\t\
    attached to the <Id>.")
    print("\t <Id> = <Exp> :: assign the lambda expression <Exp> the the\n\t\t\
    identificator <Id>. <Id> must be uppercase.")






if __name__ == '__main__':
    greeting()
    repl_loop()    

