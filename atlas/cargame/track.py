import numpy as np
from .vector import Vector

class Track:
    def __init__(
            self,
            pixels : np.ndarray
    ):
        self.pixels = pixels
    
    def get_start_position(self) -> Vector:
        """
        Looks through the pixels and finds the pixels which are rgb(255, 0, 0) and finds the start point associated with them
        Returns the (x,y) position as a vector.
        """
        
        x_positions = []
        y_positions = []
        for i in range(0, len(self.pixels)):
            for j in range(0, len(self.pixels)):
                if self.pixels[i][j] == (255, 0, 0):
                    x_positions.append(i)
                    y_positions.append(len(self.pixels -1 - i))
        return Vector((min(y_positions) + max(y_positions)) / 2, (min(x_positions) + max(x_positions)) / 2)

        # self.pixels[0][0] -> (r, g, b): (int, int, int)
        pass

    def get_state(self) -> np.ndarray:
        """
        Returns the pixels array
        """
        return self.pixels
    
    def get_end_positions(self) -> list[Vector]:
        """
        Looks through the pixels and finds all pixels which are rgb(0, 255, 0) and returns their (x,y) indices as Vectors
        """
        green_pixel_list = []
        for i in range(0, len(self.pixels)):
            for j in range(0, len(self.pixels)):
                if self.pixels[i][j] == (0, 255, 0):
                    green_pixel_list.append(Vector(j, len(self.pixels) - 1 - i))
        return green_pixel_list
        
