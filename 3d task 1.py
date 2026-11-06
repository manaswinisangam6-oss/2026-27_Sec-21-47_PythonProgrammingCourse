def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


user_input_length=int(input("enter length value:"))
user_input_breadth=int(input("enter breadth value:"))

area, perimeter = rectangle_area_perimeter(user_input_length, user_input_breadth)


print("Area:", area)
print("Perimeter:", perimeter)