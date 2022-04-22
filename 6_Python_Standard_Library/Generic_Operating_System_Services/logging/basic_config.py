import logging
"""
asctime:
Python time method asctime() converts a tuple or 
struct_time representing a time as returned by gmtime() or localtime()
to a 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'
"""
# Writing log to error_log.txt file
logging.basicConfig(#filename="error_log.txt",
                    #filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s  %(name)s %(process)d %(levelname)s : %(message)s",)

# TODO: Need to understand debug levels
# Uncomment below line to see the output
# logging.disable(level=logging.DEBUG)
logging.warning("Staring Program")


def factorial(number):
    total = 1
    for i in range(1, number+1):
        total *= i
        logging.info(f" when i is {i} total is {total}")
    return total


print(factorial(7))
logging.debug("Ending Program")

