"""
Author      : Madhu Babu Kencha
created on  : 6-10-2018


1) Iterator in python is simply an object that can be iterated upon.
   An object which will return one element at a time
2) Python iter object must implement two special methods,
   __iter__()
   __next__()
   collectively called iterator protocol
3) Python iterables are list, tuple, set, dictionary, string
4) The iter() function returns an iterator from iterable.
   It internally calls the __iter__() function
"""


def main():
    # Defining an iterable
    student_names = ["Madhu", "Arun", "Gopi"]
    # Converting an iterable to iterator
    names_iter = iter(student_names)
    # calling through casual next() function
    print(next(names_iter))
    # The above function same as
    print(names_iter.__next__())
    print(next(names_iter))
    # Calling more then iterable length causes an exception
    print(next(names_iter))


if __name__ == '__main__':
    main()
