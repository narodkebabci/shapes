import sys
import os
from math import pi
import yaml

class Circle:
    def __init__(self, radius, fill='blue', stroke='black'):
        self._radius = radius # private/protected
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        """ Calculate the area of a circle """
        return int(pi * self._radius ** 2)

    @property
    def radius(self): # public access for _radius; read only
        return self._radius

    def __len__(self):
        return int(2 * pi * self._radius)

    def __call__(self):
        return 'I am a circle!'

    def __str__(self):
        return f"A {self._fill} circle of radius {self._radius}"

def main():
    circle = Circle(5.0, fill='green', stroke='black')
    print(f'Area of the circle is {circle.calculate_area()}')
    print(f'Circumference of the circle is {len(circle)}')
    print(circle()) # return the call
    print(circle) # return the str

    my_dict = {
        'key' : {
            'inside_dict':[5,6,7,8]
        }
    }

    return 0

class Quadrilateral:
    def __init__(self, height, width, fill='grey', stroke='purple'):
        self._height = height
        self._width = width
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        """ Calculate the area of a circle """
        return int(self._height * self._width)

class Canvas:
    def __init__(self, height, width, background='lightgrey'):
        self._height = height
        self._width = width
        self._background = background

class Text:
    def __init__(self, size=16, font='Helvetica', color='darkorange'):
        """
        :param size: set a default size for text class
        :param font: set a default font for text class
        :param color: set a default color for text class
        """
        self._size = size
        self._font = font
        self._color = color

if __name__ == '__main__':
    sys.exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
