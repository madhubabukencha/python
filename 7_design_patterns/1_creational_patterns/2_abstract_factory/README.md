## Abstract Factory Design Pattern
**Abstract Factory** Pattern built on top Factory design pattern.
It provides a way to create objects of related classes without
specifying their concrete implementation. This pattern is
particularly useful when the system has to create multiple 
families of related objects without depending on their 
concrete classes.

### Participants of the Abstract Factory
- **Abstract Product**: Abstract Product declares an interface
  for a type of product object. This could be an interface or
  an abstract class with methods that are common to all 
  concrete product types.
- **Concrete Product**: Concrete Product classes implement the
  Abstract Product interface or extend the abstract class. These
  classes represent the different types of products that are 
  created by the concrete factories. Each concrete product
  belongs to a specific product family and is created by the
  corresponding concrete factory.
- **Abstract Factory**: This is an interface or an abstract class
  that declares a set of methods for creating abstract product
  objects. It defines the interface for creating the factory
  methods, which will be implemented by concrete factories.
- **Concrete Factory**: Concrete factory classes implement the
  Abstract Factory interface or extend the abstract class. These
  classes are responsible for creating concrete product objects
  as per the abstract factory's methods. Each concrete factory
  corresponds to a specific variant of products
## 