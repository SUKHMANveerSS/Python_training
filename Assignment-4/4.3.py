# Example 3
def status(age):
  if age < 0:
    raise ValueError("Only positive integers are allowed")  
  if age>22:
 		print("eligible for mrg")
  else:
 		print("not eligible for mrg try after some time")

try:
  num = int(input("Enter your age: "))
  status(num)
except ValueError:
 print("Only positive integers are allowed you ......")
finally:
 print("finally block....")

# Output 1                                                                       
# Enter your age: -12
# Only positive integers are allowed you ......
# finally block....

# Output2
# Enter your age: 25
# eligible for mrg
# finally block....