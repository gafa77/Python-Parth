# Python Polymorphism

#The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Example:
# Define a base class with a method
class Shape:
    def area(self):
        pass

# Define a subclass that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Define another subclass that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a list of shapes
shapes = [Circle(5), Rectangle(4, 6), Circle(3), Rectangle(2, 8)]

# Iterate over the list and call the area method on each shape
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()}")

# Output:
# Area of Circle: 78.5
# Area of Rectangle: 24
# Area of Circle: 28.26
# Area of Rectangle: 16

