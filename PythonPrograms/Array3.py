from numpy import *

arr = array([1,2,3,4,5])
print(arr)
arr+=5
print(arr)
arr*=5
print(arr)

arr2 = arr.copy()

print(arr)
print(id(arr))
print(arr2)
print(id(arr2))


arr[1] = 7

print(arr)
print(id(arr))
print(arr2)
print(id(arr2))