#!/usr/bin/python3/
#writes a sequence of BDD variables in dimacs CNF format
import sys

def writeBDD(variables,truths):
    #testing with variables = 1 2 ... 16, truths=8
    endvar=max(variables)
    for location in variables:
        for n in truths:
            

