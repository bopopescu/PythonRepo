# What and Why do we need it :
from abc import ABC, abstractmethod



class Computer(ABC):
    @abstractmethod
    def process1(self):
        # print('Running')
        pass

class Laptop(Computer):

    def process1(self):
        print('Running')

    def lap_Process(self):
        print('method of Laptop')


#com = Computer()
lap = Laptop()

#com.process1()
lap.lap_Process()
