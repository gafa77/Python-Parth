# Functions

#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.



# Creating a Function
#In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")

# Calling a Function
#To call a function, use the function name followed by parenthesis:

my_function()



# Return Values

#To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



# The pass Statement

#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement


