# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:11:03 2024

@author: Student
"""

#BAI 34
n=int(input('nhập n: '))

while n <= 0:
    n=int(input('nhập n: '))

if n < 2:
    print("n không phải là số nguyên tố")
    
else:
    for i in range(2, n+1):
        if n%i == 0:
            print("n không phải là số nguyên tố")
            break
        else:
            print('n là sô nguyên tố') 
            break
        