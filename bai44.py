# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:30:13 2024

@author: Student
"""

#BAI 44
s = 0
n = int(input("nhap n: "))
while n <= 0:
    n = int(input("nhap n: "))
for i in range (1, n+1):
    s += (2*i + 1)/(2*i +2)
print(round(s, 2))
