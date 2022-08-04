class A:
    def add(self,a,b):
        print(a+b)

class B:
    def multiply(self,a,b):
        print(a*b)

class C(A,B):
    def divide(self,a,b):
        print(a/b)

ob=C()
ob.add(10,30)
ob.multiply(2,5)
ob.divide(10,5)

