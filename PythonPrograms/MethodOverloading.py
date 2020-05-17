class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a,b):
        s = a+b
        return s



s1 = Student(74,78)
print(s1.sum(5,9))