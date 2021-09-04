"""
Name         : Madhu Babu Kencha
Created on   : 07-03-2019

The fromkeys() method creates a new dictionary from the given
sequence of elements with the value provided by the user.

syntax :-
dictionary.fromkeys(keys, value)
keys --> Keys to create a dictionary with
value --> Value for the key(optional)

:return :-
It returns a new dictionary with provided sequences and values
"""


def basic_example():
    sequence = ['Lion', 'Elephant', 'Giraffe']
    value = 'Animal'
    dictionary = dict.fromkeys(sequence, value)
    print("Dictionary :", dictionary, "\n")


def with_mutable_values():
    """
    If the provided values value is mutable object(like diction,list) then
    it's value will change whenever mutable object is changed
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mutable_object = [1]
    dictionary = dict.fromkeys(vowels, mutable_object)
    print("Before modifying mutable object:", dictionary)
    mutable_object.append(5)
    print("After modifying mutable object:", dictionary, "\n")


# It's not related to concept but it is worthy look at it.
def fixing_issue_with_mutable_objects():
    """
    To avoid this issue we have to create a new list from a list
    Here in the below example by using dictionary compression we will fix
    this issue.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mutable_object = [1]
    # Here for each key in keys a new list is getting created and then assigned to it
    # It seems creating a new list working a like copy function
    # we are doing some like
    # key = list(mutable_object)
    # So id of both mutable_object and key object is different
    dictionary = {key: list(mutable_object) for key in vowels}
    print("Before modifying mutable object:", dictionary)
    mutable_object.append(5)
    print("After modifying mutable object:", dictionary)
    print(f"Checking mutable object: {mutable_object}")


if __name__ == '__main__':
    basic_example()
    with_mutable_values()
    fixing_issue_with_mutable_objects()

    # from string
    vowels = dict.fromkeys("aeiou", 0)
    print(f"Vowels: {vowels}")
