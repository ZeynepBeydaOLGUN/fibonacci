# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:01:36 2020

@author: zbolg
"""

a=1
b=1
fibonacci=[a,b]
for i in range(20):   
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)
