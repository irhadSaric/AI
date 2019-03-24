from math import sqrt


class City():
    def __init__(self, id: int, x: float, y: float, neighbours: dict):
        self.id = id
        self.x = x
        self.y = y
        self.neighbours = neighbours
        self.currentValue = 0

    def __le__(self, other: 'City'):
        return self.currentValue <= other.currentValue

    def __lt__(self, other):
        return self.currentValue < other.currentValue

    @staticmethod
    def euclideanDistance2D(a: 'City', b: 'City') -> float:
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
