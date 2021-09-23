from csv import DictReader

with open("fighters_copy.csv", "r") as my_file:
    data = DictReader(my_file, delimiter="|")
    for row in data:
        print(f"Name: {row['Name']}")
