from numpy import *


m = matrix('1 2 4; 6 9 8 ; 7 5 7')
m1 = matrix('1 2 3; 7 9 8 ; 6 5 8')

print(m)
print(m.diagonal())
print(m.min())
print(m.max())

m2 = m + m1
print("Addition : ",m2)

m3 = m-m1
print("Substraction : ",m3)

m4 = m*m1
print("Multiplication :",m4)

