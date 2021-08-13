from pprint import pprint


def full_name(first_name: "First Name",
              last_name: "Last Name") -> "Full Name":
    return first_name+" "+last_name


pprint(full_name.__annotations__)