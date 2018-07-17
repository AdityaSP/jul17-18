Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print "Hello World"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?
>>> print('Hello World')
Hello World
>>> print('''Hello World''')
Hello World
>>> print("""Hello World""")
Hello World
>>> print('''Hello World
Hello Again
Hello Oracle''')
Hello World
Hello Again
Hello Oracle
>>> 
>>> print('Hello "World"')
Hello "World"
>>> print("It's a Tuesday")
It's a Tuesday
>>> 
>>> 
>>> 
>>> a = 10
>>> b = 20.3
>>> c = True
>>> d = 'hello'
>>> print(a)
10
>>> print(a,b,c,d)
10 20.3 True hello
>>> a
10
>>> a,b,c,d
(10, 20.3, True, 'hello')
>>> type(a)
<class 'int'>
>>> type(a), type(b), type(c), type(d)
(<class 'int'>, <class 'float'>, <class 'bool'>, <class 'str'>)
>>> a = d
>>> type(a)
<class 'str'>
>>> c = true
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c = true
NameError: name 'true' is not defined
>>> s = "c"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> 
>>> a = 1
>>> a + 4
5
>>> b = a + 4
>>> b
5
>>> # a++
>>> a = a + 1
>>> a += 1
>>> a
3
>>> b
5
>>> a/b
0.6
>>> c = a/b
>>> type(c)
<class 'float'>
>>> if a/b == 0:
	print("Launch Rocket")

	
>>> 
>>> d
'hello'
>>> d + " Again"
'hello Again'
>>> d + 5
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d + 5
TypeError: must be str, not int
>>> d + str(5)
'hello5'
>>> 5 + '3'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    5 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5 + int('3')
8
>>> str(5) + '3'
'53'
>>> a
3
>>> a ** 10
59049
>>> 
