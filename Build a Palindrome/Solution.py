# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:50:03 2020

@author: mohiu
"""

file = open("input.txt")
numOfInput = file.read(1)

remove = ['', " ", '\n']
def strip(f):
    for c in range(len(remove)):
        if remove[c] == f:
            f = file.read(1)
            strip(f)
    return f  

s = []
a = []
b = []

def inlist(array,size):
    for i in range(size):
        f = file.read(1)
        f = strip(f)
        array.append(f)

inlist(a,)