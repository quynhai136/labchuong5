# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:34:35 2024

@author: Student
"""

#BAI 43
s = 0
n = int(input("nhap n: "))
while n <= 0:
    n = int(input("nhap n: "))
for i in range (1, n+1):
    s += i/(i + 1)
print(round(s, 2))