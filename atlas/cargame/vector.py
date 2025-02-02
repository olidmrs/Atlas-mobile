class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def copy(self) -> "Vector":
        return Vector(self.x, self.y)
    
    def __add__(self, o: "Vector") -> "Vector":
        return Vector(self.x + o.x, self.y + o.y)
    
    def __truediv__(self, divisor: float) -> "Vector":
        return Vector(self.x / divisor, self.y / divisor)
    
    def __mul__(self, mul: float) -> "Vector":
        return Vector(self.x * mul, self.y * mul)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"