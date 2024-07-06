# Data Types

#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:

"""
Text Type      :	str
Numeric Types  :	int, float, complex
Sequence Types :	list, tuple, range
Mapping Type   :	dict
Set Types      :	set, frozenset
Boolean Type   :	bool
Binary Types   :	bytes, bytearray, memoryview
None Type      :	NoneType
"""



# Getting the Data Type

#You can get the data type of any object by using the type() function:

#Text Type
#1 string
x = "Hello World"
print(x, type(x)) 

#Numeric Types
#2 int
x = 10
print(x, type(x)) 

#3 float
x = 10.5
print(x, type(x)) 

#4 complex
x = 10j
print(x, type(x)) 

#Sequence Types
#5 list
x = ["apple", "banana", "cherry"]
print(x, type(x)) 

#6 tuple
x = ("apple", "banana", "cherry")
print(x, type(x)) 

#7 range
x = range(6)
print(x, type(x)) 

#Mapping Type 
#7 dict
x = {"name" : "John", "age" : 36}
print(x, type(x))

#Set Types
#8 set
x = {"apple", "banana", "cherry"}
print(x, type(x))

#9 frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))

#Boolean Type
#10 bool
x = True
print(x, type(x))

#Binary Types  
#11 bytes
x = bytes(5)
print(x, type(x))

#12 bytearray
x = bytearray(5)
print(x, type(x))

#13 memoryview
x = memoryview(bytes(5))
print(x, type(x))

#None Type
#14 NoneType
x = None
print(x, type(x))


#You can get the data type of any object by using the type() function:
x = 5
print(x, type(x)) 

#Method 1
x = "Hello World"
print(x, type(x)) 

#Method 2
x = str("Hello World")
print(x, type(x)) 
