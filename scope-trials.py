Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 100
>>> def finda():
	print(a)

	
>>> finda()
100
>>> def finda():
	print("GLOBALS****", globals())
	print("LOCALS*****", locals())
	print(a)

	
>>> finda()
GLOBALS**** {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 100, 'finda': <function finda at 0x0000002F0B2517B8>}
LOCALS***** {}
100
>>> def finda():
	a = 200
	print("GLOBALS****", globals())
	print("LOCALS*****", locals())
	print(a)

	
>>> finda()
GLOBALS**** {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 100, 'finda': <function finda at 0x0000002F0B251730>}
LOCALS***** {'a': 200}
200
>>> def finda():
	a = a + 100

	
>>> a
100
>>> finda()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    finda()
  File "<pyshell#13>", line 2, in finda
    a = a + 100
UnboundLocalError: local variable 'a' referenced before assignment
>>> def finda():
	global a
	a = a + 100

	
>>> a
100
>>> finda()
>>> a
200
>>> 
>>> 
>>> 
>>> 
>>> a = 100
>>> def f1():
	a = 200
	def f2():
		b = 300
		print("From F2", a, b)
	f2()
	print("From F1", a)

	
>>> f1()
From F2 200 300
From F1 200
>>> def f1():
	a = 200
	def f2():
		global a
		a = 400
		b = 300
		print("From F2", a, b)
	f2()
	print("From F1", a)

	
>>> a
100
>>> f1()
From F2 400 300
From F1 200
>>> a
400
>>> def f1():
	a = 200
	def f2():
		nonlocal a
		a = 400
		b = 300
		print("From F2", a, b)
	f2()
	print("From F1", a)

	
>>> f1()
From F2 400 300
From F1 400
>>> a
400
>>> a = 100
>>> f1()
From F2 400 300
From F1 400
>>> 
