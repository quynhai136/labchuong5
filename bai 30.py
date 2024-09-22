# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:43:46 2024

@author: Student
"""

#BAI 30
nam = int(input("nhap vao nam:"))
thang = int(input("nhap vao thang:"))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    ngay = 31
elif thang in [4, 6, 9 , 11]:
    ngay = 30 
if (nam%4 == 0 and nam %100 !=0) or (nam%400==0):
    ngay = 29
else:
    ngay = 28
print(f"{ngay}, {thang}, {nam}")