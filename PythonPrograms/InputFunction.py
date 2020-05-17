# input() --> Take input from user in runtime.
x = int(input("Enter 1st number: \n"))
y = int(input("Enter 2nd number: \n"))
z = x+y
print("Sum of the number "+str(x) + "and " +str(y) +" is : "+ str(z))

# lets go for expression
result = eval(input('Enter an expression : '))
print('Your result of expression is --> '+str(result))

# Program to find qube of an number

x = int(input('Enter any integer : '))
y = pow(x,3)

print('Qube of '+str(x)+' is : '+str(y))
