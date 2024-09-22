# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:41:06 2024

@author: Student
"""

#BAI 40
s = 0
n = int(input("nhap n: "))
while n <= 0:
    n = int(input("nhap n: "))
for i in range (1, n+1):
    s += 1/(2*i)
print(round(s, 2))