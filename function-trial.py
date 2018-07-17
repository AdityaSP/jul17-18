Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sayhi():
	print("Hi")

	
>>> sayhi()
Hi
>>> def sayhi():
	"this is a function which says a cheerful hi"
	print("Hi")

	
>>> sayhi.__doc__
'this is a function which says a cheerful hi'
>>> len.__doc__
'Return the number of items in a container.'
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> help(sayhi)
Help on function sayhi in module __main__:

sayhi()
    this is a function which says a cheerful hi

>>> help(type)
Help on class type in module builtins:

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
 |  
 |  Methods defined here:
 |  
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __dir__(...)
 |      __dir__() -> list
 |      specialized __dir__ implementation for types
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __instancecheck__(...)
 |      __instancecheck__() -> bool
 |      check if an object is an instance
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __prepare__(...)
 |      __prepare__() -> dict
 |      used to create the namespace for the class statement
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __sizeof__(...)
 |      __sizeof__() -> int
 |      return memory consumption of the type object
 |  
 |  __subclasscheck__(...)
 |      __subclasscheck__() -> bool
 |      check if a class is a subclass
 |  
 |  __subclasses__(...)
 |      __subclasses__() -> list of immediate subclasses
 |  
 |  mro(...)
 |      mro() -> list
 |      return a type's method resolution order
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __abstractmethods__
 |  
 |  __dict__
 |  
 |  __text_signature__
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __base__ = <class 'object'>
 |      The most base type
 |  
 |  __bases__ = (<class 'object'>,)
 |  
 |  __basicsize__ = 864
 |  
 |  __dictoffset__ = 264
 |  
 |  __flags__ = -2146675712
 |  
 |  __itemsize__ = 40
 |  
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |  
 |  __weakrefoffset__ = 368

>>> 
>>> 
>>> 
>>> 
>>> 
>>> def add(x,y):
	print(x+y)

	
>>> add()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    add()
TypeError: add() missing 2 required positional arguments: 'x' and 'y'
>>> add(3,4)
7
>>> x = add(3,4)
7
>>> x
>>> def add(x,y):
	return x + y

>>> m = add(3,4)
>>> m
7
>>> 
>>> 
>>> 
>>> def full_name(fn, ln):
	return fn +
SyntaxError: invalid syntax
>>>  def full_name(fn, ln):
	return fn + " " + ln
SyntaxError: unexpected indent
>>> def full_name(fn, ln):
	return fn + " " + ln

>>> full_name('Aditya', 'SP')
'Aditya SP'
>>> full_name(fn = 'Aditya', ln = 'SP')
'Aditya SP'
>>> full_name(ln = 'SP', fn = 'Aditya')
'Aditya SP'
>>> 
>>> 
>>> 
>>> def len(x):
	return 1000000

>>> s
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'Hello;
SyntaxError: EOL while scanning string literal
>>> s = 'Hello'
>>> len(s)
1000000
>>> del len
>>> len(s)
5
>>> def full_name(fn, ln, title='Mr'):
	return title + "." + fn + " " + ln

>>> full_name('Aditya','SP')
'Mr.Aditya SP'
>>> full_name('Aditya','SP','Dr')
'Dr.Aditya SP'
>>> full_name('Aditya',title='Dr', ln='SP')
'Dr.Aditya SP'
>>> 
>>> 
>>> l = ['India','China','Burma']
>>> sorted(l)
['Burma', 'China', 'India']
>>> sorted(l, reverse=True)
['India', 'China', 'Burma']
>>> import threading
>>> 
>>> 
>>> 
>>> 
>>> def any_args(*args):
	print(args)
	print(type(args))

	
>>> any_args(1,'as',45,78,34)
(1, 'as', 45, 78, 34)
<class 'tuple'>
>>> sum((1,2,3,4))
10
>>> sum([1,2,3,4])
10
>>> def adder(*args):
	return sum(args)

>>> adder(1,2,45,234,456,678,342)
1758
>>> adder()
0
>>> adder(1,2)
3
>>> 
>>> 
>>> 
>>> def any_kwargs(**kwargs):
	print(kwargs)

	
>>> any_kwargs(what='one', where='two')
{'what': 'one', 'where': 'two'}
>>> 
>>> 
>>> 
>>> # 1kg = 1.6 pounds
>>> # 1km = .6 miles
>>> # 1in = 2.54 cms
>>> 
>>> def convert(**kwargs):
	if 'kg' in kwargs:
		return kwargs['kg'] * 1.6
	elif 'km' in kwargs:
		return kwargs['km'] * 0.6
	elif 'in' in kwargs:
		return kwargs['in']* 2.54
	else:
		print("Unsupported conversion")

		
>>> convert(kg=3)
4.800000000000001
>>> convert(km = 5)
3.0
>>> convert(mts = 5)
Unsupported conversion
>>> 
