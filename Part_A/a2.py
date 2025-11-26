import math


def rectangle_area(length, width):
    return length * width


def square_area(side):
    return side * side


def circle_area(radius):
    return math.pi * radius * radius


def triangle_area(base, height):
    return 0.5 * base * height


if __name__ == "__main__":

    shape = input("Enter the shape(rectangle, square, circle, triangle):")
    invalid = False
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        area = rectangle_area(length, width)
    elif shape == "square":
        side = float(input("Enter the side of the square:"))
        area = square_area(side)
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle:"))
        area = circle_area(radius)
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle:"))
        height = float(input("Enter the height of the triangle:"))
        area = triangle_area(base, height)
    else:
        print("invalid shape")
        invalid = True
    if invalid != True:
        print(f"The area of the {shape} is {area:2f}")
