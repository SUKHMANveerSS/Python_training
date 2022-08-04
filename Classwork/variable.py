a=10
def f():
    print("inside f():",a)
    def g():
        a=20
        print("inside g():",a)
    g()

f()        


a=10
def f1():
    print("f1",a)
def g():
    a=20
    print("g",a)

def h():
    global a
    a=30
    print("h",a)

print("glo",a)
f()
print("glo",a)
g()
print("glo",a)
h()
print("glo",a)


a=10
def f():
    b=67
    print("inside f():",a)
    def g():
        a=20
        nonlocal b

        print(b)
        print("inside g():",a)
    g()
f()    
