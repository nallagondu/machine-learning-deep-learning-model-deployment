# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:06:20 2023

@author: nallag
"""

a =3
print(a)
a = "abc"
print(a)
a = 4
b = 6
print(a+b)
print(a*b)

my_list = [12,34,56,778]
print(my_list[0])
print(my_list[1])
my_list_2 = [12,'222',34]
print(my_list_2[-1])

if 3 < 4:
        print("with in if loop")
print('outside the loop')

for i in range(10):
    print(i)

print("new function0")
new_list = []
for i in my_list:
    print(i)
    new_list.append(i*3)
   # print(k)
print("new function")
    
def calculatesum(a,b):
    return a+b
print(calculatesum(12, 34655))
print("new function3")


def calculateSumandDivision(a,b):
    return a+b, a/b

var1,var2 = calculateSumandDivision(12, 14)
print(var1)
print(var2)

with open("my_file1.txt","w") as f:
    f.write("sample content 1 and write new content ")
    
with open("my_file1.txt","a") as f:
    f.write("append content 1 and write new content ")
    
with open("my_file1.txt","w") as f:
    f.write("New content 2 ")
    
import numpy as np
sample_list = [12,32,43,45,56,67]
sample_numpy_1d_array = np.array(sample_list)

sample_numpy_2d_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    
new_array = sample_numpy_2d_array.reshape(1,-1)
new_array1 = sample_numpy_2d_array.reshape(-1,1)
    
    
    
    
    
    