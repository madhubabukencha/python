from csv import DictWriter


with open("people.csv", "w", newline='') as file:
    headers = ['Name', 'Age', 'Country']
    writer_obj = DictWriter(file, fieldnames=headers)
    writer_obj.writeheader()
    writer_obj.writerows([{'Name': 'Madhu', 'Age': 25, 'Country': 'India'},
                          {'Name': 'Martin', 'Age': 56, 'Country': 'Sweden'}])

