# Python program to display the Fibonacci sequence

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


num = int(input("Enter a number: "))

# check if the number of terms is valid
if num < 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(fibonacci(i), end=" ")