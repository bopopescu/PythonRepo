
# arguments are formal arguments
# Default arguments
def person(name='Default' , age=18):
    print("Name : ",name)
    print("Age : ",age-5)
# Actual arguments
person('Souvik',29)
# Keyword arguments
person(age=29,name='Shivansh')
# Default argument example
person()

# Variable length argument
def sum(*y):
    c=0
    for i in y:
        c+=i
    print(c)

sum(100,300,12,12,3,4,5,6,7)

# Keyworded variable length argument
def persson(name,**data):
    print('Name : ',name)
    for i,j in data.items():
        print(i," : ",j)


persson('Souvik',age=29,city='Bangalore',mob=8583813520)