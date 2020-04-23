import math
import os
import random
import re
import sys

arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

def sum_array(arr,fila,col):
    suma=0
    suma+= arr[fila-1][col-1]
    suma+= arr[fila-1][col]
    suma+= arr[fila-1][col+1]
    suma+= arr[fila][col]
    suma+= arr[fila+1][col-1]
    suma+= arr[fila+1][col]
    suma+= arr[fila+1][col+1]
    return suma

sum_max=-63 #7*-9= -63 range restriction(-9,9)
for i in range(1,5):
    for j in range(1,5): 
        current_sum=sum_array(arr,i,j)
        if current_sum>sum_max:
            sum_max=current_sum
print(sum_max)
