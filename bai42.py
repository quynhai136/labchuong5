# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:36:59 2024

@author: Student
"""

s = 0
n = int(input("nhap n: "))
while n <= 0:
    n = int(input("nhap n: "))
for i in range (1, n+1):
    s += 1/i*(i + 1)
print(round(s, 2))