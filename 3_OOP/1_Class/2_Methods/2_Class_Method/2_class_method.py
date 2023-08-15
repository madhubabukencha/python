"""
Name: Madhu Babu Kencha
Date: 04-07-2021

In this program we can see how to apply class decorator

It can modify a class state that would apply across all the
instances of the class. For example, it can modify a class
variable that will be applicable to all the instances.
"""


class BirthPlace:
    birth_place = "India"

    def display(self):
        print(self.birth_place)

    # Inplace of cls, class object will come
    @classmethod
    def update_birth_place(cls, country):
        # It changes class state that would apply across all the instances of the class
        cls.birth_place = country


# Creating class method
print(BirthPlace.birth_place)
BirthPlace.update_birth_place("America")
print(BirthPlace.birth_place)

# You can also create call using an object
jack_sparrow = BirthPlace()
print(jack_sparrow.birth_place)
