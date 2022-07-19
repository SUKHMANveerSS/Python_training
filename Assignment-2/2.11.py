# Python program to find sum of elements in list

# creating an empty list
list = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input("element"+ str(i+1)+ "::"))

	list.append(ele) 
	
print(list)
total = sum(list)
print("Sum of all elements in given list: ", total)