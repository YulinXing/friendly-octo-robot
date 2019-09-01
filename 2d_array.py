import numpy as np 
from matplot lib import pyplot as plt 

arr_initial=[[80,80,255,80,80,255,80,80],\
                [80,80,255,80,80,255,80,80],\
                [255,80,120,120,120,120,255,80],\
                [255,80,255,255,255,255,80,80],\
                [255,80,120,120,120,120,80,80]]

def task1(arr):
	arr1=arr_initial.copy(arr)
	burnt_out=False
    for i in range(len(arr1)):
        for x in range(len(arr1[i])):
            arr1[i][x]*=1.1
            if arr1[i][x]==255:
                burnt_out=True
    if burnt_out==False:
        return arr1
    else:
        return True
 
def task2(arr):
	arr2=arr_initial.copy(arr)
    for i in range(len(arr2)):
        arr2[i]=arr2[i][::-1]
    return arr2

 def task3(arr):
 	arr3=arr_initial.copy(arr)
 	MaxVal=int(input("Max value:"))
 	for i in range(len(arr3)):
 		for x in range(len(arr3[i])):
 			if arr3[i][x]>MaxVal:
 				arr3[i][x]=MaxVal
 	return arr3
