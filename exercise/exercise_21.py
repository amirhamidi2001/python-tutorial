class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width: int, height: int):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def set_width(self, width: int):
        """Set the width of the rectangle."""
        self.width = width

    def set_height(self, height: int):
        """Set the height of the rectangle."""
        self.height = height

    def get_area(self) -> int:
        """Return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """Return the length of the rectangle's diagonal."""
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        """Return a string picture of the rectangle using '*' characters.

        If width or height is larger than 50, returns a warning string.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape) -> int:
        """Return how many times `shape` can fit inside this rectangle."""
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self) -> str:
        """Return string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Represents a square, subclass of Rectangle."""

    def __init__(self, side: int):
        """Initialize square with side length."""
        super().__init__(side, side)

    def set_side(self, side: int):
        """Set the side length of the square."""
        self.width = side
        self.height = side

    def set_width(self, width: int):
        """Set the width (and height) of the square."""
        self.set_side(width)

    def set_height(self, height: int):
        """Set the height (and width) of the square."""
        self.set_side(height)

    def __str__(self) -> str:
        """Return string representation of the square."""
        return f"Square(side={self.width})"
