

class Car:
    # Variable declared outside init is Class variable
    # Whereas Class variables are stored in class namespace
    wheels = 4

    def __init__(self):
        # Variables declared inside init is a instance variable.
        # Instance variables are stored in instance namespace
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

c1.mil = 20

print(c1.com,c1.mil,Car.wheels)
print(c2.com,c2.mil,Car.wheels)
