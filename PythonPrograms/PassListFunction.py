

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = [12,31,24,54,10,34,65,7,54,89,45,67,23,44,67]

even,odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))