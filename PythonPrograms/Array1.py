from array import *

vals = array('i',[5,8,9,4,2])

# Address and size
print(vals.buffer_info())
print(vals.typecode)
vals.reverse()
print(vals)


print(vals[0])

for i in vals:
    print(i)


arr = array('i',[])
n=int(input("Enter the length of the array : "))

for i in range(n):
    x=int(input("Enter the next value : "))
    arr.append(x)

print(arr)
searchVal = int(input("which value you want to search? "))
index=0
for i in arr:
    if i==searchVal:
        print("Match found at ",index," st/nd/rd/th position")
        break
    index+=1
else:
    print("No match found!")

print(arr.index(searchVal))

