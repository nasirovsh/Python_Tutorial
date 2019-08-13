"""
Classmethods use case #1: Factory Methods
Factory methods are those methods which return a class object (like constructor) for different use cases.
Here classmethod used as decorator
"""
from datetime import date

#random Person
class Person:	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, birthYear):
		return cls(name, date.today().year - birthYear)

	def display(self):
		print(self.name + "'s age is: " + str(self.age))

person = Person('Adham', 19)
person.display()

person1 = Person.fromBirthYear('Eshmat', 1986)
person1.display()				
		