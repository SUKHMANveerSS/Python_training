# Example 9

class Vehicle:
 	def __del__(self):
 	    print("Vehicle object destroyed")
 	    print(10/0)
v = Vehicle()
del v
# Output
# Vehicle object destroyed
# Exception ignored in: <function Vehicle.__del__ at 0x0000023AE69FA440>
# Traceback (most recent call last):
#   File "c:\Users\Guneet kaur\python\training\assignment4\assi4_q9.py", line 6, in __del__
#     print(10/0)
# ZeroDivisionError: division by zero