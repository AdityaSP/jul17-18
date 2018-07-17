Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 4
>>> if a < 10:
	print("Single digit")

	
Single digit
>>> a = 11
>>> if a < 10:
	print("Single digit")

	
>>> if a < 10:
	print("Single digit")
else:
	print("May be double digit")

	
May be double digit
>>> if a < 10:
	print("Single digit")
elif a < 100:
	print("Double digit")
else:
	print("2 + digits")

	
Double digit
>>> l = ['India','USA','UK']
>>> l.index('USA')
1
>>> l.count('USA')
1
>>> if l.count('USA') > 0:
	print("USA exists")

	
USA exists
>>> if 'USA' in l:
	print("USA Exists")

	
USA Exists
>>> s = 'hello world'
>>> 'd' in s
True
>>> 'wor' in s
True
>>> 'USA' in l
True
>>> x = 3
>>> y = 5
>>> x > 3 and y < 10
False
>>> x == 3 and y < 10
True
>>> x > 3 or y < 10
True
>>> x > 3
False
>>> not x > 3
True
>>> 
>>> 
>>> x = 5
>>> x > 3 and x < 10
True
>>> 3 < x < 10
True
>>> y = 8
>>> x > 3 and x < y and y < 20
True
>>> 3 < x < y < 20
True
>>> 
>>> 
>>> l
['India', 'USA', 'UK']
>>> count = 0
>>> while count < len(l):
	print(l[count])
	count += 1

	
India
USA
UK
>>> for country in l:
	print(country)

	
India
USA
UK
>>> for x in l:
	print(x)

	
India
USA
UK
>>> l
['India', 'USA', 'UK']
>>> 
>>> 
>>> 
>>> if a < 100:
	if a < 50:
		if < 10:
			
SyntaxError: invalid syntax
>>> if a < 100:
	if a < 50:
		if a < 10:
			print("Less than 10")
		print("Less than 50")
	print("Less than 100")

	
Less than 50
Less than 100
>>> a
11
>>> 
>>> 
>>> 
>>> 
>>> 
