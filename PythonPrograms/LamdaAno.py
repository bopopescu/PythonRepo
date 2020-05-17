from functools import reduce

f = lambda a : a*a

result = f(5)
print(result)

f1 = lambda a,b : a+b
result = f1(7,8)
print(result)

def is_even(n):
    return n%2 ==0

nums = [3,2,5,6,7,8,1,2,3,4,5,6,7,8,9]

# Filter - (functions,Iterable)
evens = list(filter(is_even,nums))
odd = list(filter(lambda  n:n%2!=0,nums))
print(evens)
print(odd)

# Map - (functions,Iterable)
doubles_even = list(map(lambda n:n*2,evens))
print(doubles_even)

# Reduce
sum = reduce(lambda a,b:a+b,doubles_even)
print(sum)