class Field:
    def __init__(self, rect, x, y):
        self.rect = rect
        self.x = x
        self.y = y
        self.visited = False
        self.ship_placed = False
        self.value = 0

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return "("+self.x+", "+self.y+")"

    def __repr__(self):
        return "(" + str(self.x)+ ", " + str(self.y)+ ")"