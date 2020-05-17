

class Student:
    school = 'UNIV'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # Accessor method
    def get_m1(self):
        return self.m1

    # Mutator method
    def set_m1(self, value):
        self.m1 = value

    # Class method
    # When we are operate on instance variable we use 'self' and for Class variables we use 'cls' keyword
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static method --> Not operating with any instance or class variable so it's a static method
    @staticmethod
    def info():
        print("This is Student class")




s1 = Student(36,67,89)
s2 = Student(50,70,79)


print(s1.avg())
print(s2 .avg())





