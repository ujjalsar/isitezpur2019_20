# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:24:27 2019

@author: gupta
"""

from os import makedirs
from os.path import join, exists


student_names = """abhinash
abhinav
abhishek
akhilesh
anurima
ashutosh
avnish
bishal
dhritiman
dristanta
gunjan
harshajyoti
kankan
karishma
kuldeepdoley
kuldeepkumar
prakarti
roshan
saheed
satyajit
shreyasee
subham
sumedha
ujjal
shyamalendu
"""

def create_dir():
    path = "D:\dev\GitHub\isitezpur2019_20\isitezpur2019_20"    
    students = student_names.splitlines()
    #print(students)
    for each_stu in students:
        #print(each_stu)
        folder_path = join(path , each_stu)
        if not exists(folder_path):
            makedirs(folder_path)
            print("created", each_stu)
        else:
            print("not created", each_stu)
        
        stu_folder = join(folder_path, "__init__.py")
        with open(stu_folder, "w") as fp:
            fp.write("#" + each_stu)
        

    



if __name__ == "__main__":
    create_dir()

