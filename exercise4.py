# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:15:07 2023

@author: s_liebaert20
"""

quad_zahl = [1,2,3,4,5,6,7,8,9,10]
for k in range(1, 11):
    if k % 2 == 0: 
        print(k)
    else: 
        print(k**2)
 
quad_zahl = [1,2,3,4,5,6,7,8,9,10]
for k in range(11):
    if k % 2 == 0:
        quad_zahl.append(k)
    else :
        quad_zahl.append(k**2)
quad_zahl


