# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:23:12 2024

@author: Student
"""

#BAI 45
s = 0
ts = 0
ms = 1
n = int(input("nhap n: "))
while n <= 0:
    n = int(input("nhap n: "))
x = float(input("nhap x: "))
for i in range (1, n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(round(s, 2))
