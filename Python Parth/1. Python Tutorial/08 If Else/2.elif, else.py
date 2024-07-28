# Elif

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".



# Else

#The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



#In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

#You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#This technique is known as Ternary Operators, or Conditional Expressions.

#You can also have multiple else statements on the same line:

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")


# And

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# saame for OR and NOT



# The pass Statement

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
