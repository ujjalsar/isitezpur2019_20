- lambda functions
- file operations
- exception handling
- examples of code in class, inheritance, constructor, destructor, 
- generators, decorators, list comprehensions, 
- file operations,  modules, __main__, namespace, context manger
- builtin module
- Introduction on Numpy, Pandas
- Matrix operations


# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:32:37 2019

@author: gupta
"""


"""
def f1(*args, **kwargs):
    a,b,c = args
    x,y,z = kwargs["x"],kwargs["y"],kwargs["z"] 
    t = a*x + b*y + c*z
    print(t)
    

f1(10,20,30, x=100, y=200, z=300)

mystr = "Hello I am from tezpur"

print(mystr)
ln = len(mystr)
print(mystr[::-1])
"""


L1 = [1,2,3,4]		
L2 = [5,6,7,8]
l3 = list(zip(L1, L2))

l4 = list()
for x in l3:
    print(x)
    l4.append( list(x) )

print(l4)




















