# https://realpython.com/python-walrus-operator/
f = lambda x: x+1
data = [1, 2, 3, 4]
f_data = [y for x in data if (y := f(x)) != 4]
print(f_data)