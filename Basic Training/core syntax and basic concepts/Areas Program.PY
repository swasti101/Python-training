# shape = input("Enter the shape :  \n Press \n1 for Rectangle \n2 for Circle  ")
# if(shape.isnumeric() == False):
#     print("Enter valid number")
# elif(shape == "1"):
#     length = input("Enter length:")
#     breadth = input("Enter breadth:")
#     if(length.isnumeric() == False):
#         print("Enter a numeric value")
#     if(breadth.isnumeric() == False):
#         print("Enter a numeric value")
#     area = int(length)*int(breadth)

#     print("Area of Rectangle is",area,"m^2")
# elif(shape == "2"):
#     radius = input("Enter Radius :")
#     if(radius.isnumeric() == False):
#         print("Enter a numeric value")
#     print("Area of circle is",(3.14)*float(radius)*float(radius),"m^2")
# else:
#     print("Enter either 1 or 2")

import math

def calculate_area():
    try:
        shape = input("Enter the shape (rectangle/circle): ")
        
        if shape == "rectangle":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive numbers.")
            area = length * width
            print(f"Area of the rectangle: {area}")
    
        elif shape == "circle":
            radius = float(input("Enter the radius: "))
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            area = math.pi * (radius ** 2)
            print(f"Area of the circle: {area}")
        
        else:
            print("Invalid shape entered.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    finally:
        print("Program execution completed.")



calculate_area()






