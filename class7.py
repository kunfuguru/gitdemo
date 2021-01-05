
class A:

    def __init__(self):
        print("in A Test")

class B:

    def __init__(self):
        print("in B")


class C(A,B):

    def __init__(self):
        print("in C")
        super().__init__()






a1 = A()
b1 = B()
c1 = C()