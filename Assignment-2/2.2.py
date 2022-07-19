num = int(input("Enter a number: "))

 factorial = 1

# # check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
 else:
    for i in range(1,num + 1):
        factorial = factorial*i
print("The factorial of",num,"is",factorial)