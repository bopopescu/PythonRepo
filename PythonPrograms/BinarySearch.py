from math import *

pos = -1
list = [11,12,21,32,43,54,65,76,87,98,109,209,309,409]
n = int(input("Enter any integer to search : "))

def binarySearch(list,n):
    list.sort()
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


if binarySearch(list,n):
    print('Match Found at ',pos+1)
else:
    print('No match')








