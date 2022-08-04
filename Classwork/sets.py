set={10,20,30,"name"}
for x in set:
    print(x)

set.add("roll no.")    
print(set)

set.remove(30)
print(set)

set={10,20,30,40}
f=frozenset(set)
print(f)
print(type(f))