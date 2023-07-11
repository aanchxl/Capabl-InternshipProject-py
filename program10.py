# Define a function to calculate the area of a rectangle
def area(length, width):
    area = length * width
    return area

# Call the function with arguments and print the result
a= int(input("Enter length of rectangle: "))
b= int(input("Enter width of rectangle: "))
rectangle_area =area(a,b)
print("The area of the rectangle is:", rectangle_area)
