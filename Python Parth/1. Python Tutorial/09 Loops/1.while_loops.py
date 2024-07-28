# While Loops

#Loops

"""
Python has two primitive loop commands:

1. while loops
2. for loops
"""



# while Loop

#With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1


#   Remember to increment i, or else the loop will continue forever. (infinite loop)

#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.



# break Statement

#With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1



# continue Statement

#With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result



# else Statement

#With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


