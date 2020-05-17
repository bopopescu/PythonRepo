

def factorial(num):
    fact =1
    for i in range(1,num+1):
        fact *=i
    print(fact)

factorial(4)


def factRecurrsion(n):
    if n==0:
        return 1
    else:
        return n*factRecurrsion(n-1)

result = factRecurrsion(5)
print(result)