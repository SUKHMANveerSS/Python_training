class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Guneet kaur', 19)

print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(21)

print('Name:', stud.name, stud.get_age())