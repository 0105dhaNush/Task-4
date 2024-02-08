import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
    
    def calculate_area(self):
        areas = [math.pi * (r ** 2) for r in self.radius_list]
        return areas
    
    def calculate_circumference(self):
        circumferences = [2 * math.pi * r for r in self.radius_list]
        return circumferences

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

print("Areas of circles:", areas)
print("Circumferences of circles:", circumferences)
