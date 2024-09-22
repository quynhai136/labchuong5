# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:47:09 2024

@author: Student
"""

#BAI 37
s = 0
n = int(input("nhap n(phai la so chan): "))
while n <= 0 or n%2 != 0:
  n = int(input("nhap n: "))
for i in range (2, n+1, 2):
    s += i
print(" tong S =", s)
