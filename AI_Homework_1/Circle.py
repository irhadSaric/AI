from AI_Homework_1.Point import Point


class Circle:
    def __init__(self, center: 'Point', radius: int):
        self.center = center
        self.radius = radius
        self.movable = True

    def __repr__(self):
        return "(" + str(self.center.x) + ", " + str(self.center.y) + "), " + str(self.radius) + str(self.movable)

    @staticmethod
    def intersects(f1: 'Circle', f2: 'Circle') -> bool:
        if f1.radius + f2.radius >= f1.center.euclidean_distance_2D(f2.center):
            return True
        return False