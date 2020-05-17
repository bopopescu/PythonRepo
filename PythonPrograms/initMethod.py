

class Computer:

# like constructor in python
    def __init__(self,cpu='AMD',ram=90):
       # print("in init")
        self.cpu = cpu
        self.ram = ram


# we are biniding our data with every method
    def config(self):
        print("Config is : ",self.cpu,self.ram)



com1 = Computer()
com2 = Computer('i5',32)

com1.config()
com2.config()

