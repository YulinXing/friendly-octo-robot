#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:54:37 2019

@author: timxing
"""

tickettype=input("ticket type:")

while (tickettype!='E') and (tickettype!='S'):
    tickettype=input("ticket type:")
    
weight=int(input("baggage weight:"))
Erate=3.5
Eallowance=16
Srate=5.75
Sallowance=20

if(tickettype=='E'):
    excess=weight-Eallowance
    if(excess>=0):
        charge=excess*Erate
else:
    excess=weight-Sallowance
    if(excess>=0):
        charge=excess*Srate

print(charge)
    
    
