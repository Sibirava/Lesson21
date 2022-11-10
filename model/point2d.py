import math

class Point2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property  #обычный геттер
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @x.deleter
    def x(self):
        del self._x

    @property  # обычный геттер
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @y.deleter
    def y(self):
        del self._y

    def calculate_distance(self, point):
        if not isinstance(point, Point2D):
            return -1

        return math.sqrt((self._x - point.x)**2
                         + (self._y - point.y)**2)

    def __str__(self):
        return f"Point ({self.x}; {self.y})"