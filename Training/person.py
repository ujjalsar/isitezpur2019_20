# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:48:07 2019

About: 

@author: gupta
"""

class Person:
    """
    sdjlfdsj
    """
    #lname = ""
    #fname = ""
    def __init__(self, lname, fname):
        self.lname = lname
        self.fname = fname
    
    def __str__(self):
        return self.lname + ", " + self.fname

class Employee(Person):
    def __init__(self):
        Person.__init__(self, "haranadh", "gupta")
        self.salary = 10000

    def get_salary(self):
        print("eligible for salary")

    def get_bonus(self):
        print("eligible for bonus")
        
    def __get_secret_code(self):
        return 100000
        
class PEmployee(Employee):
    def __init__(self):
        Employee.__init__(self)

class COther:
    def __init__(self):
        print("contractor related base")
    
class Contractor(Employee, COther):
    def __init__(self):
        Employee.__init__(self)
        COther.__init__(self)

    def get_bonus(self):
        print("Not eligible")
    
if __name__ == "__main__":
    p1 = Person("Haranadha", "Gupta")
    p1.fname = "Haranadha"
    p1.lname = "Gupta"
    p1.salary =  5000
    
    print(p1)
    
    p2 = Person("", "")
    p2.fname = "rajiv"
    p2.lname = "ghosh"
    print(p2)
    
    p3 = Employee()
    p3.fname = "rajiv"
    p3.lname = "ghosh"
    print(p3)    
    
    p4 = PEmployee()
    
    print(p4)
    p4.get_bonus()

    p5 = Contractor()
    
    print(p5)
    p5.get_bonus()
    
    print(p3.__get_secret_code()) # throws error.
    print(p3.fname, p3.lname, p3.salary)
    


