"""
Classmethods use case #2: Correct instance creation in inheritance
Whenever you derive a class from implementing a factory method as a class method, it ensures correct instance creation of the derived class.
You can create a static method for the classmethod_1 but the object it creates, will always be hardcoded as Base class.
But, when you use a class method, it creates the correct instance of the derived class.
"""
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@staticmethod
	def fromFathersAge(name, fatherBirthYear, fatherPersonAgeDiff):
		return Person(name, date.today().year - fatherBirthYear + fatherPersonAgeDiff)

	@classmethod	
	def fromBirthYear(cls, name, birthYear):
		return cls(name, date.today().year - birthYear)

	def display(self):
		print(self.name + "'s age is: " + str(self.age))	 


class Man(Person):
	sex = 'male'


man = Man.fromBirthYear('Max', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('Max', 1965, 20)
print(isinstance(man1, Man))
