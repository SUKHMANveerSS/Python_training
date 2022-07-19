# Python program to find average max and min elements in list

# creating an empty list
list = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input("element"+ str(i+1)+ "::"))
	list.append(ele) 
	
print(list)
b=min(list)
c=max(list)
d=sum(list)/len(list)
print('MINIMUM ELEMENT IN A LIST IS',b,
'\nMAXIMUM ELEMENT IN A LIST IS ',c,
'\nAVERAGE IS',d)