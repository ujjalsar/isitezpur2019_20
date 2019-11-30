# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:11:21 2019

@author: gupta
"""

class A:
    def __init__(self, i=100):
        self.i = i

class B(A):
    def __init__(self, j=20):
        self.j = j
        
        
b = B()

#print(b.j)



def main():
    pass


if __name__ == "__main__":
    main()
    
    
