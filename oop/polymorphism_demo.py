import math

# Base class: Shape
class Shape:
    def area(self):
        # Placeholder for derived classes to override
        raise NotImplementedError("Subclasses must override this method")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Formula: length * width
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Formula: π * radius^2
        return math.pi * (self.radius ** 2)
