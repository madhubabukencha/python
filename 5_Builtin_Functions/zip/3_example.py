# A small practical application

student_names = ["Ravi", "James", "Newton", "Flyman", "Ramanujan"]
marks = [67, 34, 56, 67, 100]
mapped = (zip(student_names, marks))

for nm, mr in mapped:
    print(f"Name : {nm} \t\t Marks : {mr}")
