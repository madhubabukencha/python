import re 
nameAge = '''Madhu age is 21,Rama age is 22 ,Krishna age is 23 ,Narayana age is 24'''
age = re.findall(r'\d{1,2}', nameAge)
print(age)
# finding all strings starting with Capital letter
# followed by strings
name = re.findall(r'[A-Z][a-z]*', nameAge)
print(name)
details = {}
index = 0
for allName in name:
    details[allName] = age[index]
    index += 1
print(details)
