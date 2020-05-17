class A:
    def __init__(self):
        print('Constructor of A')

    def feature1(self):
        print('Feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')

class B(A):
    def __init__(self):
        super().__init__()
        print('Constructor of B')
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')

class C:
    def __init__(self):
        print('Constructor of C')

    def feature3(self):
        print('Feature 3C is working')

class D(C,B):

    pass


d1 = D()


