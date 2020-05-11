# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:35:00 2020

@author: mohiu
"""

file = open("input.txt")

remove = ['', " ", '\n']

def strip(f):
    for c in range(len(remove)):
        if remove[c] == f:
            f = file.read(1)
            strip(f)
    return f  

def inlist(array,size):
    for i in range(size):
        f = file.read(1)
        f = strip(f)
        array.append(f)
    #return array
        
n = []
m = []
a = []
A = []
B = []

inlist(n,1)
inlist(m,1)
inlist(a,int(str(n[0])))
inlist(A,int(str(m[0])))
inlist(B,int(str(m[0])))

postive = set(a) & set(A)
negative = set(a) & set(B)
happiness = len(postive) - len(negative)
print(happiness)
