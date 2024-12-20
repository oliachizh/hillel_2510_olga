class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Create two points
point1 = Point(1, 2)
point2 = Point(3, 4)

# Add the points
result = point1 + point2
print(result)  # Output: Point(4, 6)
