class Circle:
    _pi = 3.141  # Private class variable for pi

    def __init__(self, radius_list):
        self.radius_list = radius_list

    @classmethod
    def area(cls, radius):
        return cls._pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls._pi * radius

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]

for radius in radius_list:
    circle_area = Circle.area(radius)
    circle_perimeter = Circle.perimeter(radius)
    print(f"Circle with radius {radius}: Area = {circle_area}, Perimeter = {circle_perimeter}")
