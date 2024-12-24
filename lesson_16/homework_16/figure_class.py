from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        NotImplementedError(f'calculate_area method is not implemented')

    @abstractmethod
    def calculate_perimeter(self):
        NotImplementedError(f'calculate_perimeter method is not implemented')

class Square(Figure):
    def __init__(self, side_length):
        self._side_length = side_length
    def __str__(self):
        return 'Square'

    def calculate_area(self):
        return self._side_length**2


    def calculate_perimeter(self):
        return self._side_length*4

class Rectangle(Figure):
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def __str__(self):
        return 'Rectangle'

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2*(self._width + self._length)


figures = [Square(5), Rectangle(3, 5)]

for figure in figures:
    print(f"Here is the area of {figure}: {figure.calculate_area()}")
    print(f"Here is the perimeter of {figure}: {figure.calculate_perimeter()}")