#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:20:10 2019

@author: timxing
"""

row=int(input("num:"))

while (row%2==0):
    row=int(input("please input an odd num:"))
 
sym=input("symbol:")

space=(row-1)//2
symbols = 1
for i in range(1, row + 1, 2):
    print(" " * space, end='')
    for k in range(1, symbols + 1):
        print(sym, end='')
    print("")
    symbols += 2
    space -= 1