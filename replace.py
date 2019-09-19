#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:20:45 2019

@author: timxing
"""

fr=open("qbdata.txt","r")
fw=open("newqbdata.txt","w")
sym=str(input("character:"))
num=0

for i in range(34):
    line=fr.readline()
    if(line[num]==" "):
        line[num]==sym
        i=i+1
        fw.write(line)
    if(line[num]=="\n"):
        i=0

        
fr.close()
fw.close()


