import string

values = dict(name="Madhu Babu Kencha", age=22, salary=200000)

details = string.Template("""
Name        : $name
Age         : $age
Salary      : $salary
""")
print("PERSONAL DETAILS :", details.substitute(values))
