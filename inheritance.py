Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class LB():
	def breathe():
		print("I breathe")

		
>>> class HB():
	def breathe():
		print("I breathe")

		
>>> class LB():
	def breathe():
		print("I breathe")

		
>>> class HB(LB):
	pass

>>> obj = HB()
>>> obj.breathe()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    obj.breathe()
TypeError: breathe() takes 0 positional arguments but 1 was given
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> class HB(LB):
	pass

>>> obj.breathe()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    obj.breathe()
TypeError: breathe() takes 0 positional arguments but 1 was given
>>> obj = HB()
>>> obj.breathe()
I breathe
>>> class HB(LB):
	def metathink(self):
		print("I think therefore I am")

		
>>> obj = HB()
>>> obj.breathe()
I breathe
>>> obj.metathink()
I think therefore I am
>>> class HB(LB):
	def breathe(self):
		print("Through lungs")
	def metathink(self):
		print("I think therefore I am")

		
>>> obj = HB()
>>> obj.breathe()
Through lungs
>>> obj.metathink()
I think therefore I am
>>> class LB():
	def breathe():
		print("I breathe")

		
>>> class HB(LB):
	def breathe(self):
		print("Through lungs")
	def metathink(self):
		print("I think therefore I am")

		
>>> class LB():
	def breathe():
		print("I breathe")

		
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> class HB(LB):
	def breathe(self):
		LB.breathe(self)
		print("Through lungs")
	def metathink(self):
		print("I think therefore I am")

		
>>> obj = HB()
>>> obj.breathe()
I breathe
Through lungs
>>> obj.metathink()
I think therefore I am
>>> 
>>> 
>>> 
>>> 
>>> l = [12,32,56]
>>> l[4]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l[4]
IndexError: list index out of range
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> ValueError
<class 'ValueError'>
>>> len
<built-in function len>
>>> err = ValueError()
>>> raise err
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    raise err
ValueError
>>> raise ValueError('Insufficient balance')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    raise ValueError('Insufficient balance')
ValueError: Insufficient balance
>>> 
