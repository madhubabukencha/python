# Factory
Factory method is a creational design pattern that focuses on object creation.
They provide a central location for creating objects instead of scattered creation
logic throughout the code. This central location, called a factory, is responsible
for deciding which type of object to create based on some criteria and then returning
the newly created object. Decoupling of object creation from client code is a core
principle of the Factory Method Pattern. It falls under the Gang of Four (GoF) design
patterns and is widely used to promote loose coupling within an application.

**Main components of the Factory Method Pattern**:
- Product Interface/Class: Defines the common characteristics of all objects to be created.
- Concrete Product Classes: Implement the Product interface/class for different types of objects.
- Factory Class: Acts as the central control system, responsible for deciding and creating objects based on specific criteria.
- The client code that needs an object does not specify the concrete class of the object. It relies on the factory method or interface to create the object.

**Benefits**:
- Loose Coupling: The code using the factory doesn't need to know about the specific concrete product classes being created. This makes the code more flexible and adaptable.
- Open/Closed Principle: Adding new product types requires only implementing a new concrete product class and registering it with the factory, without modifying existing code.
- Centralized Object Creation: Simplifies managing object creation logic and makes it easier to track and change how objects are created.

**Types of Factory Patterns**:
- Factory Method: Provides an interface for creating objects, but lets subclasses decide which specific type to create.
- Abstract Factory: Creates families of related objects, ensuring consistency within each family.
- Singleton Factory: Creates and controls access to a single instance of a particular object.

**Real-world Examples:**
- Database connection creation: A factory can create different database connections based on the requested database type (MySQL, PostgreSQL, etc.).
- UI widget creation: A factory can create different UI widgets (buttons, text boxes, etc.) based on the user interface layout.
- Document format conversion: A factory can create different document format converters (PDF, Word, etc.) based on the input file format.
