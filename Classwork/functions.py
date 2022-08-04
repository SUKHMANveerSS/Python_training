def disp(a,b,c):
    d=a+b+c
    print(d)
disp(10,20,30)    

def names(*d):
    print(d[2])
names("tehal","sukhman","nimish") 




def names(**d):
    print(d["name2"])
names(name1="tehal",name2="sukhman",name3="nimish")    



def disp(a,b):
    c=a+b
    return(c)
res=disp(10,20)    
print(res)
