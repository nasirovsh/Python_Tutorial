"""
The classmethod() method returns a class method for the given function.

The syntax of classmethod() method is:

classmethod(function)
classmethod() is considered un-Pythonic so in newer Python versions, you can use the @classmethod decorator for classmethod definition.

The syntax is:

@classmethod
def func(cls, args...)

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.
The class method can be called both by the class and its object.

Class.classmethod()
Or even
Class().classmethod()
But no matter what, the class method is always attached to a class with first argument as the class itself cls.

def classMethod(cls, args...)

"""

class Person:
    age = 25

    def printAge(cls):
        print('The age is: ', cls.age)

# create  printAge class method
Person.printAge = classmethod(Person.printAge)
Person.printAge()
