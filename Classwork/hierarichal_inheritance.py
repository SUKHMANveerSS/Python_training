class A:
    def f1(self):
        print("name")

class B(A):
    def f2(self):
        print("university")

class C(A):
    def f3(self):
        print("roll no.")

ob=C()
ob_1=B()
ob.f1()
ob.f3()
ob_1.f1()
ob_1.f2()