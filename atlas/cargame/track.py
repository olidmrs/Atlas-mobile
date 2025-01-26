import numpy as np
from vector import Vector
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
        pixel_list_i = []
        pixel_list_j = []
        #for i in range(0, len(self.pixels) + 1):
            #for j in range(1, len(self.pixels) + 1):

        print(self.pixels)