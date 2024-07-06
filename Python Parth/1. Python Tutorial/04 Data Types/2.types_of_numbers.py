# Numbers

"""
There are three numeric types in Python:

1. int
2. float
3. complex

Variables of numeric types are created when you assign a value to them:
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))



#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


#Float can also be scientific numbers with an "e" to indicate the power of "10".
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



# Type Conversion

#You can convert from one type to another with the int(), float(), and complex() methods:

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Note: You cannot convert complex numbers into another number type.



# Random Number

#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

#Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))
