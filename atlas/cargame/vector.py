class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def copy(self) -> "Vector":
        return Vector(self.x, self.y)