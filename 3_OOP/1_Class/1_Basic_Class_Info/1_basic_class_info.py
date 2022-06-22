"""
Author     : Madhu Babu Kencha
created on : 22-09-2018

Approaching problems by creating an object are called Object Oriented
programming.
An object(example: parrot ) have two properties
   I)   Attributes ---> Name, Age, Color, Height
   II)  Behaviour  ---> Singing, Dancing, playing

A class is a blue print of an object. "class" keyword is
used to create a class. From class we construct instances.
An instance is a specific object created from particular
class. Below a class created with name Animal.
Eg :- class Animal:
      pass

An object(instance) is an instantiation of a class
Eg :- parrot = Animal()
"""


class Animal:
    # Class attributes or class variable
    species = "animal"
    forest_area = 10000
    instance_count = 0

    def __init__(self, name, age, weight):
        """
        The __init__() method called as Constructor
        It is used to save some data. In place of self
        instance object(eg:lion) was passed.

        'name', 'age' and 'weight' are classed attributes
        also called "instance variable"

        The instance method called whenever class object called

        :param name:
        :param age:
        :param weight:
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
        If we don't pass "self" as first argument then at time of
        calling through an object we get below error
        TypeError: message() takes 0 positional arguments but 1 was given
        :return:
        """
        print("Below are the animal, {} details".format(self.name))
        print("Name \t\t\t: {0}".format(self.name))
        print("Life span\t\t: %d Years" % self.age)
        # calling class variable
        print(f"Forest Area\t\t: {Animal.forest_area}")
        # other way
        # print(self.forest_area)


# Instance count before creating object
print(f"Instance count before object creation: {Animal.instance_count}")

# Creating an object called lion
# Here name of the class acts a function
lion = Animal("Lion", 20, 400)
# output: <class '__main__.Animal'>
# print(type(lion))
lion_1 = Animal("Lion", 20, 400)

# Instance count after creating object
# Output is 2 because we have two object
print(f"Instance count After object creation: {Animal.instance_count}")

# Accessing class attributes
print("Below are {} details".format(lion.__class__.species))
# print("{}".format(Animal.species))

# Calling class method
lion.message()
# Another way of calling method
# Animal.message(lion)

# Accessing instance attributes
print("Animal weight\t: %s KG" % lion.weight)

# Adding a new variable to object
lion.type = "Wild"
print(f"Animal type\t\t: {lion.type}")

# Deleting object variable
# del lion.weight
# print(lion.weight)

