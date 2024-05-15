
# Creating a class

class Shape:
    def __init__(self, length, width):
        self.length = length #attribute 1
        self.width = width #attribute 2

    def calculate_perimeter(self): # this is our first method
        return (self.length+ self.width) * 2

my_custom_shape = Shape(50, 20) # first object 
custom_shape_2 = Shape(30, 10)
custom_shape_3 = Shape(60, 25)
custom_shape_4 = Shape(100, 50)

print(f"The length of my_custom_shape is {my_custom_shape.length}")
print(f"The width of my_custom_shape is {my_custom_shape.width}")


print(custom_shape_2.calculate_perimeter())
print(my_custom_shape.calculate_perimeter())
