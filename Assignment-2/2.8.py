pie = 3.14


def area_triangle():
    area = b*h/2
    print("\n Area of a Rectangle is: %.2f" % area)


def area_rect():
    area = l*b
    print("\n Area of a Rectangle is: %.2f" % area)


def area_sq():
    area = s*s
    print("\n Area of a Rectangle is: %.2f" % area)


def area_circle():
    area = pie*r*r
    print("Area of a circle = %.2f" % area)


print("ENTER YOUR CHOICE::")
print("1.CIRCLE")
print("2.RECTANGLE")
print("3.SQUARE")
print("4.TRIANGLE")
while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            r = float(input("Enter the radius of a circle:"))
            area_circle()

        elif choice == '2':
            l = float(input('Enter the Length of a Rectangle: '))
            b = float(input('Enter the Breadth of a Rectangle: '))
            area_rect()

        elif choice == '3':
            s = float(input('Enter the Side of a Square: '))
            area_sq()

        elif choice == '4':
            b = float(input('Enter the base of a triangle: '))
            h = float(input('Enter the Height of a triangle: '))
            area_triangle()

        next_calculation = input("Do you want t continue (y/n): ")
        if next_calculation == "n":
            print("YOU ARE EXITING!!!")
            break

    else:
        print("Invalid Input")