#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:40:46 2019

@author: timxing
"""

code=str(input('code:'))
f=open('qbdata.txt','r')
n=0
for i in range(33):
    line=f.readline()
    if code in line:
        print(line)
        break
    else:
        n+=1
        
f.close()     