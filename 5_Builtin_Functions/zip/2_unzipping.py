# This program is about unzipping a zipped map

names = ["Madhu", "Robert", "Martin"]
marks = [70, 80, 90]

mapped = list(zip(names, marks))
print(f"Zipped iterators : \n{mapped}")
print("")

print("Unzipping mapped iterators : ")
names, marks = zip(*mapped)
print(f"Names : {names}")
print(f"Marks : {marks}")
