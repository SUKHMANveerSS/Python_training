str = input("Enter a string : ")
new_str = str[-1:] + str[1:-1] + str[:1]
print(new_str)