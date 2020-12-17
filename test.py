class A:
    def print(self):
        print("AAA")


class B(A):
    def print(self):
        print("BBB")


class C(A):
    def print(self):
        print("CCC")


class D(C, B):
    pass


d = D()
d.print()
