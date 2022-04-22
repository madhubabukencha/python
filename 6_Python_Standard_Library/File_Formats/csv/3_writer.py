from csv import reader, writer


# Reading data to write to new csv file
with open("fighters.csv", "r") as read_file:
    data = reader(read_file)
    # We wouldn't able to use above data object out this scope because file is closed
    # So, we are creating new object to read out side this with scope
    data_list = list(data)

# For appending use 'a' option
with open("dummy.csv", "w") as writer_file:
    # To write, we need to create writer object
    write_obj = writer(writer_file)
    for row in data_list:
        # Methods available with write_objs are writerows(rows), writerow(row)
        write_obj.writerow(row)
