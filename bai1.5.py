# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:46:22 2024

@author: Student
"""

#BAI 46
#2*x + 7*1 + 9*1 = 979 => x = (979 - (7+9))/2 = 488.5 (499)
 
#2*1 + 7*y + 9*1 = 979 => x = (979 - (2+9))/7 = 138.5 (140)

#2*1 + 7*1 + 9*z = 979 => x = (979 - (2+7))/9 = 108 (109-110)

bo_nghiem = []
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem += [(x, y, z)]
if bo_nghiem:
    print(f' {bo_nghiem}')
    
 












 