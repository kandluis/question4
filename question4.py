from numpy import *

def funprogram():
    arr = array([[3,2,1,2,3,4],
                 [2,3,4,1,4,5],
                 [4,1,4,5,2,4],
                 [3,1,2,1,4,5],
                 [5,3,6,3,2,4],
                 [24,53,23,4,3,0])
    
    return dot(arr,arr)