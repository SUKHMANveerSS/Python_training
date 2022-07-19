# Python program to reverse list

# creating an empty list
list = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input("element"+ str(i+1)+ "::"))
	list.append(ele) 
	
print("Before Reversing :", list)

# Reversing using the reverse() method
list.reverse()
print("After Reversing :", list)

# Reversing using the slice operator
Reversed_List = list[ : : -1]
print("After Reversing :", Reversed_List)