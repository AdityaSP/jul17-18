Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'Hello World'
>>> s * 5
'Hello WorldHello WorldHello WorldHello WorldHello World'
>>> print("-" * 50)
--------------------------------------------------
>>> s
'Hello World'
>>> len(s)
11
>>> s[0]
'H'
>>> s[4]
'o'
>>> s[10]
'd'
>>> s[len(s) -1]
'd'
>>> s[11]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[11]
IndexError: string index out of range
>>> s[-1]
'd'
>>> s[-3]
'r'
>>> s[-11]
'H'
>>> s
'Hello World'
>>> s[-12]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[-12]
IndexError: string index out of range
>>> 
>>> 
>>> s[0]
'H'
>>> 
>>> 
>>> s
'Hello World'
>>> #s[<start> : <end>]
>>> s[0:5]
'Hello'
>>> s[0:3]
'Hel'
>>> s[6:200]
'World'
>>> s[-1:-10]
''
>>> s[-10:-1]
'ello Worl'
>>> s[-1:-10]
''
>>> #s[<start> : <end> : <stepper>]
>>> s[0:3:1]
'Hel'
>>> s[-1:-10:-1]
'dlroW oll'
>>> s
'Hello World'
>>> #s[-1:-11:-1]
>>> len(s)
11
>>> s[-1:-11:-1]
'dlroW olle'
>>> s[-1:-12:-1]
'dlroW olleH'
>>> s[-1:-len(s) -1: -1]
'dlroW olleH'
>>> s[6:1000]
'World'
>>> s[6:]
'World'
>>> s[0:5]
'Hello'
>>> s[:5]
'Hello'
>>> s[:]
'Hello World'
>>> s[::1]
'Hello World'
>>> s[::-1]
'dlroW olleH'
>>> s[::-1]
'dlroW olleH'
>>> s1 = s[::-1]
>>> s
'Hello World'
>>> s1
'dlroW olleH'
>>> s2 = s1[::-1]
>>> s2
'Hello World'
>>> s[::-1][::-1]
'Hello World'
>>> 
>>> 
>>> 
>>> # sequence
>>> # index based
>>> # slicing
>>> # len
>>> # index out of range
>>> s
'Hello World'
>>> s.startswith('H')
True
>>> s.startswith('Hello')
True
>>> s.upper()
'HELLO WORLD'
>>> s.lower()
'hello world'
>>> s.title()
'Hello World'
>>> s
'Hello World'
>>> s1 = s.upper()
>>> s1
'HELLO WORLD'
>>> 
>>> 
>>> 
>>> s = 'the discovery of India'
>>> s.split()
['the', 'discovery', 'of', 'India']
>>> s.split(" ")
['the', 'discovery', 'of', 'India']
>>> s = '06/18/2013  06:07 PM             4,014 xwizard.dtd'
>>> s.split()
['06/18/2013', '06:07', 'PM', '4,014', 'xwizard.dtd']
>>> s.split(" ")
['06/18/2013', '', '06:07', 'PM', '', '', '', '', '', '', '', '', '', '', '', '', '4,014', 'xwizard.dtd']
>>> s
'06/18/2013  06:07 PM             4,014 xwizard.dtd'
>>> s = 'Hello World'
>>> s[:]
'Hello World'
>>> s[::1]
'Hello World'
>>> s[::2]
'HloWrd'
>>> s[::3]
'HlWl'
>>> s[::-1]
'dlroW olleH'
>>> s[::-2]
'drWolH'
>>> s = 'the discovery of India'
>>> s.split()
['the', 'discovery', 'of', 'India']
>>> x = s.split()
>>> type(x)
<class 'list'>
>>> s = 'hareesh S'
>>> s.split()
['hareesh', 'S']
>>> 
