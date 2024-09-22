# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:46:05 2024

@author: Student
"""

#BAI 36
s = 0
n = int(input("nhap n: "))
while n <= 0:
  n = int(input("nhap n: "))
for i in range (1, n+1):
    s += i*i
print(" tong S =", s)