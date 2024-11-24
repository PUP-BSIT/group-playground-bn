import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    return math.pi  * (radius ** 2)

radius = int(input("Enter radius: "))
result = calculate_circle_area(radius)