from numpy import *

arr1=array([
    [1,2,3,7],
    [4,5,6,12]

])
# Convert multi dimension to 1-D
arr2= arr1.flatten()

print(arr1)
# Type of array
print(arr1.dtype)
# Dimension of array
print(arr1.ndim)
# will return tuple consisting the size
print(arr1.shape)
print(arr1.size)
print(arr2)

arr3 = arr2.reshape(3,4)
print(arr3)

arr4 = arr2.reshape(2,2,3)
print(arr4)

