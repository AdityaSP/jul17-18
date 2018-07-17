Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = { 'name' : 'Aditya', 'email' : 'sp.aditya@gmail.com'}
>>> type(d)
<class 'dict'>
>>> len(d)
2
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Aditya'
>>> d['email']
'sp.aditya@gmail.com'
>>> d['city']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d['city']
KeyError: 'city'
>>> d['city'] = 'Bangalore'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Bangalore'}
>>> 
>>> d['city'] = 'Mysore'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore'}
>>> d.items()
dict_items([('name', 'Aditya'), ('email', 'sp.aditya@gmail.com'), ('city', 'Mysore')])
>>> d.keys()
dict_keys(['name', 'email', 'city'])
>>> d.values()
dict_values(['Aditya', 'sp.aditya@gmail.com', 'Mysore'])
>>> 
>>> 
>>> for k,v in d.items():
	print (k,v)

	
name Aditya
email sp.aditya@gmail.com
city Mysore
>>> 
>>> 
>>> 'city' in d
True
>>> 'Mysore' in d.values()
True
>>> 
>>> d.get('phone','NA')
'NA'
>>> d.get('city','NA')
'Mysore'
>>> numd = {1:1, 2:4, 3:9}
>>> numd[1]
1
>>> numd[]
SyntaxError: invalid syntax
>>> numd[2]
4
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore'}
>>> d['phone'] = ['0182302198','9080808322']
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore', 'phone': ['0182302198', '9080808322']}
>>> d.phone
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d.phone
AttributeError: 'dict' object has no attribute 'phone'
>>> d['phone']
['0182302198', '9080808322']
>>> d['phone'][1]
'9080808322'
>>> 
>>> 
>>> d['address'] = { 'work': 'askldjou qwouq', 'home':'alsjdljas'}
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Mysore', 'phone': ['0182302198', '9080808322'], 'address': {'work': 'askldjou qwouq', 'home': 'alsjdljas'}}
>>> d['address']['work']
'askldjou qwouq'
>>> 
