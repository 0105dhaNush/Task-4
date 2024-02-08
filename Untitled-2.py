class Circle:
    _pi = 3.141  # Private class variable for pi

    def __init__(self, radius_list):
        self.radius_list = radius_list
        self.areas = []
        self.circumferences = []

    def calculate_area(self):
        self.areas = [Circle._pi * (r ** 2) for r in self.radius_list]
        return self.areas

    def calculate_circumference(self):
        self.circumferences = [2 * Circle._pi * r for r in self.radius_list]
        return self.circumferences

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

print("Areas of circles:", areas)
print("Circumferences of circles:", circumferences)
