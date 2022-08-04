class School:
    def f1(self):
        print("students names:")

class student1(School):
    def f2(self):
        print("sukhman")

class student2(School):
    def f3(self):
        print("tehal")

class student3(student1,School):
    def f4(self):
        print("tejbir")

ob=student3()
ob.f1()
ob.f2()

