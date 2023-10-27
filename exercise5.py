# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:55:30 2023

@author: s_liebaert20
"""

import matplotlib.pyplot as plt


a = 1  
r = 0.5 
n = 10  

s_n = []  

y = a
for k in range(n):
    s_n.append(y)
    y *= r 
s_n[1]

import matplotlib.pyplot as plt

plt.plot(s_n)