# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:21:48 2019

@author: gupta
"""

from keyword import iskeyword

#NPS = 50,000
HSBC = 50,000
Home = 30,000

AMEX = 14676 + 8000
HDFC = 3000 + 5000


print("hara")



print(iskeyword("otherwise"))


print(iskeyword("if"))


print(iskeyword("untill"))



class Person:
    def __init__(self, id):
        self.id = id
        
        
p1 = Person(100)
p1.__dict__["ha"] = 10

print(p1.__dict__, len(p1.__dict__), p1.ha)
