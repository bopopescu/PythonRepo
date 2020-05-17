class Student:


    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print('Name : {}  and RollNo : {}'.format(self.name,self.rollNo))

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 32



s1 = Student('Souvik',1)
s2 = Student('Shivansh',1)

s1.show()

s1.lap.brand

lap1 = s1.lap
lap2 = Student.Laptop()

print(id(lap1))
print(id(lap2))
