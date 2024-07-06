# Arbitrary Arguments, *args

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arbitrary Arguments are often shortened to *args in Python documentations.




# Keyword Arguments

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.




#  Arbitrary Keyword Arguments, **kwargs

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.



# Default Parameter Value

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



# Passing a List as an Argument

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



# Positional-Only Arguments

#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)


#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)


#But when adding the , / you will get an error if you try to send a keyword argument:
"""
def my_function(x, /):
  print(x)

my_function(x = 3)
"""



# Keyword-Only Arguments

#To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)

#Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)

my_function(3)


#But when adding the *, / you will get an error if you try to send a positional argument:

"""
def my_function(*, x):
  print(x)

my_function(3)
"""



# Combine Positional-Only and Keyword-Only

#You can combine the two argument types in the same function.
#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)