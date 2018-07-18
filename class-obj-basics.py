Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = int()
>>> type(a)
<class 'int'>
>>> l = list()
>>> l
[]
>>> l.append(1)
>>> class Car():
	pass

>>> a = int()
>>> city = Car()
>>> type(a), type(city)
(<class 'int'>, <class '__main__.Car'>)
>>> print __name__
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(__name__)?
>>> print(__name__)
__main__
>>> 
>>> 
>>> 
>>> 
>>> dir(city)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> city.name = 'City'
>>> dir(city)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
>>> city.name
'City'
>>> city.brand = 'Honda'
>>> dir(city)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'name']
>>> city.brand, city.name
('Honda', 'City')
>>> city2 = Car()
>>> dir(city2)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> 
>>> 
>>> 
>>> class Car():
	def __init__(self):
		print("In Here")

		
>>> city = Car()
In Here
>>> class Car():
	def __init__(self):
		print("In Here", id(self))

		
>>> city = Car()
In Here 547270802008
>>> id(city)
547270802008
>>> class Car():
	def __init__(self):
		print("In Here", id(self))
		self.name = 'City'
		self.brand = 'Honda'

		
>>> city=Car()
In Here 547273342648
>>> dir(city)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'name']
>>> camry = Car()
In Here 547273432704
>>> camry.brand, camry.name
('Honda', 'City')
>>> class Car():
	def __init__(self, n, b):
		print("In Here", id(self))
		self.name = n
		self.brand = b

		
>>> city = Car('City', 'Honda')
In Here 547273432648
>>> camry = Car('Camry', 'Toyota')
In Here 547270802008
>>> city.brand, city.name
('Honda', 'City')
>>> camry.brand, camry.name
('Toyota', 'Camry')
>>> class Car():
	def __init__(self, n, b):
		print("In Here", id(self))
		self.name = n
		self.brand = b
	def drive(self):
		print("I drive", self.name, self.brand)

		
>>> c = Car('City', 'Honda')
In Here 547273432704
>>> c.drive()
I drive City Honda
>>> t = Car('Camry', 'Toyota')
In Here 547273432200
>>> t.drive()
I drive Camry Toyota
>>> 
