import sys
import os
from math import pi

class Circle:
    def __init__(self, radius, fill='blue', stroke='black'):
        self._radius = radius # private/protected
        self._fill = fill
        self._stroke = stroke

    @property
    def radius(self): # public access for _radius; read only
        return self._radius

    def __len__(self):
        return int(2 * pi * self._radius)

    def __call__(self):
        return 'I am a circle!'

    def calculate_area(self):
        """ Calculate the area of a circle """
        return int(pi * self._radius ** 2)

def main():
    circle = Circle(5.0, fill='green', stroke='black')
    print(f'area = {circle.calculate_area()}')
    print(f'circumference is {len(circle)}')
    return 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
