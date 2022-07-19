# ****Pattern 1******
x = 5
for x in range(1, x + 1):
    for y in range(1, x + 1):
        print(x, end=' ')
    print('')


# *****Pattern 2*******
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()


# *******Pattern 3******
x = 6

for x in range(x):
    
    for j in range(x):
        
        print("*", end=' ')
   
    print('')


# *******Pattern 4*******
size = 5
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    
    m = m - 1
    for j in range(0, i + 1):
        print("$ ", end=' ')
    print(" ")
    

    
