# Classes and Objects

#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.



# Create a Class

#To create a class, use the keyword class:

class MyClass:
  x = 5

print(MyClass)



# Create Object

#Now we can use the class named MyClass to create objects:

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


# Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.



# The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

