"""
Author     : Madhu Babu Kencha
created on : 22-09-2018
Last updated on: 20-sep-2025

Approaching problems by creating an object is called Object-Oriented
programming.
An object(example: lion ) have two properties
   I)   Attributes ---> Name, Age, Color, Height
   II)  Behaviour  ---> Singing, Dancing, playing

A class is a blueprint of an object. "class" keyword is
used to create a class. From class we construct instances.
An instance is a specific object created from particular
class. Below a class created with name Animal.
Eg :- class Animal:
      pass

An object(instance) is an instantiation of a class
Eg :- lion = Animal()
"""


class Animal:
    """
    A class to represent an Animal.
    """
    # Class attributes or class variables. These are shared by all instances
    # of this class. These can be accessed by class.variable or instance.variable
    species = "animal"
    forest_area = 10000
    instance_count = 0

    def __init__(self, name, age, weight):
        """
        The __init__() method called as Constructor .It is used to save some
        data. In place of 'self', instance object(eg:lion) was passed.

        'name', 'age' and 'weight' are called attributes also called "instance
         variable"

        The instance method called whenever class object called and it is unique
        to each instance(object).

        :param name: Name of the animal
        :param age: Age of the animal
        :param weight: Weight of the animal
        """
        # Which equal to object.name = name
        self.name = name
        self.age = age
        self.weight = weight

        # Now it is specific to one instance(object) call
        # self.instance_count += 1

        # It is for all instance(all objects) calls
        # So it will increases as instances of this increases increases
        Animal.instance_count += 1

    def message(self):
        """
        If we don't pass "self" as first argument then at time of calling
        through an object we get below error.

        TypeError: message() takes 0 positional arguments but 1 was given

        :return: None
        """
        print(f"Below are the animal, {self.name} details:")
        print(f"Life span\t\t: {self.age} Years")
        # calling class variable
        print(f"Forest Area\t\t: {Animal.forest_area}")
        # other way
        # print(self.forest_area)


print("*" * 20 + "Creating objects" + "*" * 20)
print(f"Instance count before object creation: {Animal.instance_count}")
# Creating an object called lion. Here name of the class acts a function
lion = Animal("Lion", 20, 400)
# print(type(lion))
# output: <class '__main__.Animal'>
lion_1 = Animal("Lion", 20, 400)
print(f"Instance count after creating 2 objects: {Animal.instance_count}")


print("*" * 20 + "Accessing class attributes" + "*" * 20)
print(f"Below are `{lion.__class__.species}` details")
print(f"Forest area: {Animal.forest_area}")
print(f"Forest area: {lion.forest_area}")


print("*" * 20 + "Accessing instance methods" + "*" * 20)
lion.message()
# Another way of calling method by passing object as input
# Animal.message(lion)


print("*" * 20 + "Accessing instance attributes" + "*" * 20)
print(f"Animal weight\t\t: {lion.weight} KG")
# Adding a new variable to object
lion.category = "Wild"
print(f"Animal category(new)\t: {lion.category}")

# Deleting object variable
# del lion.weight
# print(lion.weight)
