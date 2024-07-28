# Global Scope

#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)


# Naming Variables
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


# Global Keyword

#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
