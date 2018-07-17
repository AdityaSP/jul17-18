Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> li = [1,2,3]
>>> li
[1, 2, 3]
>>> t = ('India','Burma', 'China')
>>> len(t)
3
>>> type(t)
<class 'tuple'>
>>> t[0]
'India'
>>> t[1]
'Burma'
>>> t[1:]
('Burma', 'China')
>>> t[4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
>>> t
('India', 'Burma', 'China')
>>> t[0] = 'SL'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t[0] = 'SL'
TypeError: 'tuple' object does not support item assignment
>>> t = ('India','Burma', 'China')
>>> t = 'India','Burma', 'China'
>>> type(t)
<class 'tuple'>
>>> t
('India', 'Burma', 'China')
>>> a,b,c = t
>>> a
'India'
>>> b
'Burma'
>>> c
'China'
>>> 
>>> 
>>> 
>>> a
'India'
>>> b
'Burma'
>>> a,b = b,a
>>> a
'Burma'
>>> b
'India'
>>> 
>>> 
>>> names = [('Bill', 'Gates'),('Steve', 'Jobs'),('Satya','Nadela')]
>>> type(names)
<class 'list'>
>>> len(names)
3
>>> names[1]
('Steve', 'Jobs')
>>> for name in names:
	print("Fn", name[0], "LN", name[1])

	
Fn Bill LN Gates
Fn Steve LN Jobs
Fn Satya LN Nadela
>>> for name in names:
	fn, ln = name
	print("Fn", fn, "LN", ln)

	
Fn Bill LN Gates
Fn Steve LN Jobs
Fn Satya LN Nadela
>>> for fn, ln in names:
	print("Fn", fn, "LN", ln)

	
Fn Bill LN Gates
Fn Steve LN Jobs
Fn Satya LN Nadela
>>> 
>>> 
>>> 
>>> l = [(1,2,3), (4,5,6)]
>>> t = ([1,2,3], [4,5,6])
>>> 
>>> l
[(1, 2, 3), (4, 5, 6)]
>>> l.append(34)
>>> l
[(1, 2, 3), (4, 5, 6), 34]
>>> l.pop(0)
(1, 2, 3)
>>> l
[(4, 5, 6), 34]
>>> 
>>> t = ([1,2,3], [4,5,6])
>>> 
>>> t[0].append(4)
>>> t
([1, 2, 3, 4], [4, 5, 6])
>>> t[1].pop()
6
>>> t[1].pop()
5
>>> t[1].pop()
4
>>> t
([1, 2, 3, 4], [])
>>> 
>>> 
>>> 
>>> 
