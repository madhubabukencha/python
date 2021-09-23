class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name.replace(' ', '').lower()}.{self.last_name.lower()}@email.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, value):
        name_list = value.split(" ")
        *first, last = name_list
        self.first_name = " ".join(first)
        self.last_name = last


if __name__ == '__main__':
    employee_1 = Employee("Madhu Babu", "Kencha")
    print(employee_1.email)
    print(employee_1.fullname)

    employee_1.fullname = "Mahesh Babu Kencha"
    print(employee_1.email)
    print(employee_1.fullname)
