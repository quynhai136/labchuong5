# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:28:20 2024

@author: Student
"""

#BAI 35
s = 0
n = int(input("nhap n: "))
while n <= 0:
  n = int(input("nhap n: "))
for i in range (1, n+1):
    s += i
print(" tong S =", s)
    
  