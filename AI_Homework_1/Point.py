from math import sqrt
from sys import maxsize

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):

        self.x = x
        self.y = y

    def __lt__(self, other: 'Point'):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def euclidean_distance_2D(self, b: 'Point') -> float:
        return sqrt((b.x - self.x)**2 + (b.y - self.y)**2)

    def between2D(self, p1: 'Point', p2: 'Point') -> bool:
        return min(p1.x, p2.x) <= self.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= self.y <= max(p1.y, p2.y)

    @staticmethod
    def orientation2D(a: 'Point', b: 'Point', c: 'Point'):
        p1: Point = b - a
        p2: Point = c - a

        crossProduct = p1.x * p2.y - p1.y * p2.x

        if crossProduct > 0:
            return 1 # Left orientation, counter clockwise direction
        elif crossProduct < 0:
            return 0 # Right orientation, clockwise direction
        else:
            return -1 # Colinear points

class EventPoint(Point):
    def __init__(self, eventType: str, point: 'Point', circle: 'Circle'):
        super().__init__(point.x, point.y)
        self.eventType = eventType
        self.circleIdentifier = circle