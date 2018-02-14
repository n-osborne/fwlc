#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:program name: fwlc
:module author: Nicolas Osborne <nicolas.osborne@etudiant.univ-lille1.fr>
:date: 2018, February

:synopsis: REPL for Fun With Lambda Calculus
"""



PROMPT = "<°λ°> " 
DIC = dict()

while True:
    
    command = input(PROMPT).split()

    if command[0] == ":q" or command == ":quit":
        print("Goodbye!")
        break

    elif (command[0] in (":h", ":help")) and len(command) == 1:
        printHelp() # TODO function printHelp

    elif command[0] in (":h", ":help"):
        printHelp(command[1]) # TODO function printHelp

    elif command[0][0] != ":" and len(command) == 1:
        try:
            print(read(command[0])) # TODO function read
        except:
            print("I do not understand.")

    elif command[0][0] != ":" and len(command) == 3 and command[1] == "=":
        try:
            DIC[command[0]] = read(command[2]) # TODO function read
        except: # TODO capture different exceptions (the two sides of the binary
            # operator =
            print("That does not seem to be a correct lambda expression.")
















