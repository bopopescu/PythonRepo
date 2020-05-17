

a=5
b=0

try:
    print('Resource open')
    print(a/b)

except Exception as e:
    print("You can not divide by zero. -->", e)

finally:
    print('Resource closed')


