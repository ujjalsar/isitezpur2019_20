# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:56:42 2019

@author: gupta
"""



def get_line1(afile):
    with open("some_file.txt") as fp:
        for line in fp.readlines():
            print(line)

def get_line2(afile):
    lines = []
    with open("some_file.txt") as fp:
        line = fp.readline()
        while(line):
            line = fp.readline()
            if line != "":
                lines.append(line)
    return lines

def get_line3(afile):
    with open("some_file.txt") as fp:
        line = fp.readline()
        while(line):
            line = fp.readline()
            if line != "":
                yield line
        


if __name__ == "__main__":
    afile = "some_file.txt"
    for line in get_line3(afile):
        
        print(line)

