#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:16:01 2019

@author: timxing
"""

name=str(input("name:"))
fr=open('qbdata.txt','r')
line=fr.readlines()
fw=open('newqbdata.txt','w')
for i in line:
    if name in line:
        continue
    fw.write(i)
fr.close()
fw.close()