from numpy import *


arr = array([1,4,6,8,2,1,64,23])
arr = array([1,4,6,8,2,1,64,23.0])
print(arr)
print(arr.dtype)

arr1 = linspace(1,100,100)
print(arr1)

arr2 = arange(0,100,2)
print(arr2)

arr3= logspace(1,40,5)
print(arr3)

arr4 = zeros(5)
print(arr4)

arr5 = ones(5,int)
print(arr5)