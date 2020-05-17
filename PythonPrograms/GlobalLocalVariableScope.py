

a=10

def something():
    a = 15
    x = globals()['a']
    # local variable
    print("in function : ",a)
    print("in function : ",id(a))

something()

# global variable
print("outside : ",a)
print("outside : ",id(a))

