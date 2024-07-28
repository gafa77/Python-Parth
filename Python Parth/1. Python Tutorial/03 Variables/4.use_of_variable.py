# Output Variables

#The Python print() function is often used to output variables.


#In the print() function, you output single or multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".


#You can also use the + operator to output multiple variables:

x = 5
y = 10
print(x + y)

#Note you can only add(+) same datatype of variables. If you try to combine a string and an integer, Python will throw you an error:

"""
x = 5
y = "John"
print(x + y)
"""

#But you can write with commas.
x = 5
y = "John"
print(x, y)



# Global Variable

#Variables that are created outside of a function are known as global variables. 
#Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



# Global Keyword

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
