from csv import reader
import logging

# To avoid dependency on print statements
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
# To debug this program just comment below line
logging.disable(logging.DEBUG)

with open("fighters.csv", "r") as my_file:
    data = reader(my_file)
    # We can also convert data into list of lists
    # my_list = list(data)
    logging.debug(data)
    # Skipping headers section
    next(data)
    # Here a row is a list
    for row in data:
        logging.debug(row)
        print(f"fighter '{row[0]}' is from '{row[1]}'")
