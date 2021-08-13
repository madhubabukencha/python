class Employee:
    def __init__(self, pan_card, name):
        self.__pan_card = pan_card
        self.__name = name


employee_1 = Employee(232234, "Madhu Babu Kencha")

# print(employee_1.__pan_card)
print(employee_1.__dict__)

# getattr() method helps to getting attributes of a class
print(getattr(employee_1, "_Employee__pan_card"))

# Accessing attributes which are not present but you need to provide default value too
# or else it will through AttributeError
print(getattr(employee_1, "sex", "Male"))