class name:
    def f1(self):
        print ('sukhman')

class address(name):
    def f2(self):
        print("ludhiana")

ob = address()
ob.f1()
ob.f2()

class name:
    a=10
    b=20
    def __init__(self,a,b):
        print('A')
    
    def f1(self):
        print("sukhman")            

class address(name):
    a=4
    b=5
    def __init__(self):
        super().__init__(12,12)

    def f2(self):
        super().f1()
        print(self.a,self.b)
        print(super().a,super().b)

ob=address()
ob.f1()
ob.f2()        