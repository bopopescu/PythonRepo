

file = open("MyData.txt",'r')

#print(file.readline())
#print(file.readline())
##print(file.readlines())
#print(file.readable())
#print(file.read())

file1 = open('abc.txt','w')
#file1.write('Something ')
#file1.write('People ')
#file1.write('Laptop ')


#file1 = open('abc.txt','a')
#file1.write('Append')

for data in file:
    file1.write(data)
    print(data)
