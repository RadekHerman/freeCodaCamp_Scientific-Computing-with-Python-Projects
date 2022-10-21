#######
### Scientific Computing with Python Projects 
### Polygon Area Calculator
### https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
#######



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Additionally, if an instance of a Rectangle is represented as a string,
    # it should look like: Rectangle(width=5, height=10)
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, x):
        if isinstance(self, Square):
            self.width = x
            self.height = x
        else:
            self.width = x

    def set_height(self, y):
        if isinstance(self, Square):
            self.height = y
            self.width = y
        else:
            self.height = y

    # get_area: Returns area (width * height)
    def get_area(self):
        return self.width * self.height

    # Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    # Returns a string that represents the shape using lines of "*".
    # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
    # There should be a new line (\n) at the end of each line.
    # If the width or height is larger than 50, this should return the string: "Too big for picture.".
    def get_picture(self):
        full_picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for _ in range(self.height):
            line = "*" * self.width + "\n"
            full_picture += line
        return full_picture

    # Takes another shape (square or rectangle) as an argument.
    # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
    # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

    def get_amount_inside(self, obj):
        return int(self.width / obj.width) * int(self.height / obj.height)


# The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in.
# The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
# The Square class should be able to access the Rectangle class methods but should also contain a set_side method.
# If an instance of a Square is represented as a string, it should look like: Square(side=9)
# Additionally, the set_width and set_height methods on the Square class should set both the width and height.


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    # set_side method
    def set_side(self, x):
        self.width = x
        self.height = x
