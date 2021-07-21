>>> 5
5
>>> 5*7
35
>>> str('Zoot!')
'Zoot!'
>>> str(b'Zoot!')
"b'Zoot!'"
>>> str(Zoot!)
SyntaxError: invalid syntax
>>> x=str('zoot!')
>>> x
'zoot!'
>>> x.capitalize()
'Zoot!'
>>> if 1:
	print("True")

	
True

>>> if 1:
	print("True")

	print("Done")

>>> if 1:
	print("True")
print("Done")
SyntaxError: invalid syntax
>>> if 1:
	print("True")

print("Done")
SyntaxError: invalid syntax
>>> if 1:
	print("True")

 print("Done")
 
SyntaxError: unindent does not match any outer indentation level

>>> if 1:
	{print("True");}
	
SyntaxError: invalid syntax

>>> x=5
>>> y=10
>>> total = x + y
>>> total
15
>>> total = x +
SyntaxError: invalid syntax
>>> total = x + \
	y
>>> total
15

#Vaiables
>>> x=10
>>> x="test"
>>> x
'test'
>>> x=10
>>> x
10

#Environment Path
>>> import sys
>>> print(sys.path)

#System Path
>>> exec(open('C:/Users/aislam/Dropbox/APythonCode/sql.py').read())

# py C:/Users/aislam/Dropbox/APythonCode/sql.py

#
>>> lst = []
>>> lst
[]
>>> lst = [1,2,3,4]
>>> lst
[1, 2, 3, 4]
>>> lst.append(5)
>>> lst
[1, 2, 3, 4, 5]
>>> help(lst.append)
Help on built-in function append:

append(...) method of builtins.list instance
    L.append(object) -> None -- append object to end

>>> 


