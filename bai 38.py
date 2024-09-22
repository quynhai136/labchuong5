# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:00:49 2024

@author: Student
"""

# BAI 38
s = 1
n = int(input("nhap n(phai la so le): "))
while n <= 0 or n%2 == 0:
  n = int(input("nhap n: "))
for i in range (1, n+1):
    s *= i
print(" tong S =", s)
