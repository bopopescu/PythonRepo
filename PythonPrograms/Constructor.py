class Computer :

    def __init__(self):
        self.name = 'Souvik'
        self.age = 29

    def updateAge(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print('They are same',c1.age,' ',c2.age)


c1.name = 'Shivansh'
c1.age=0.5
c1.updateAge()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)