from matplotlib import pyplot as plt 

arr_initial=[[80,80,255,80,80,255,80,80],
            [80,80,255,80,80,255,80,80],
            [255,80,120,120,120,120,255,80],
            [255,80,255,255,255,255,80,80],
            [255,80,120,120,120,120,80,80]]

def task1(arr):
    burnt_out=False
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            arr[i][x]*=1.1
            if arr[i][x]==255:
                burnt_out=True
                
    if burnt_out==False:
        return arr
    else:
        return True
 
def task2(arr):
    for i in range(len(arr)):
        arr[i]=arr[i][::-1]
    return arr

def task3(arr):
    MaxVal=int(input("Max value:"))
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            if arr[i][x]>MaxVal:
                arr[i][x]=MaxVal
    return arr

fig,(ax1,ax2,ax3)=plt.subplots(1,3)        
ax1.imshow(task1(arr_initial),cmap='gray',vmin=0,vmax=255)
ax2.imshow(task2(arr_initial),cmap='gray',vmin=0,vmax=255)
ax3.imshow(task3(arr_initial),cmap='gray',vmin=0,vmax=255)
plt.show()            
