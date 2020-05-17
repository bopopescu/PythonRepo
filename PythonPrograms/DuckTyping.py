# so duck typing is something where --> ide type can be anything but only condition it has to get the execute method.
# like it can switch to MyEditor class object from PyCharm if and only if both the class have 'execute' method.

class PyCharm:
    def execute(self):
        print('compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('compiling')
        print('Running')

class Laptop:
    def code(self,ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)