

class Computer:

    def config(self):
        print("i5, 16gb, 1TB")



com1 = Computer()
com2 = Computer()

# So com1 or com2 object are passed as argument for config method
Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()