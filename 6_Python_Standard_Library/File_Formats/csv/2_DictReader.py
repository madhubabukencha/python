from csv import DictReader
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
# To debug this program just comment below line
# logging.disable(logging.DEBUG)
with open("fighters_copy.csv", "r") as my_file:
    data = DictReader(my_file, delimiter="|")
    logging.debug(data)
    # Here a row is dictionary
    for row in data:
        logging.debug(row)
        print(f"Name: {row['Name']}")
