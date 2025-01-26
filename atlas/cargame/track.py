import numpy as np
from .vector import Vector

class Track:
    BAD_TILE = (0, 0, 0)
    START_TILE = (255, 0, 0)
    END_TILE = (0, 255, 0)
    ROAD_TILE = (255, 255, 255)

    def __init__(
            self,
            pixels : np.ndarray
    ):
        self.pixels = pixels
        print("Getting Start Pixel List")
        red_pixels = self.get_start_pixel_list()
        print("Got Start Pixel List")
        y_pixels = [pix.y for pix in red_pixels]
        x_pixels = [pix.x for pix in red_pixels]

        car_height = max(y_pixels) - min(y_pixels)
        car_width = max(x_pixels) - min(x_pixels)
        self.car_dimensions = Vector(car_width, car_height)

    @classmethod
    def pix_equal(cls, pix: list[int], other: list[int]) -> bool:
        return pix[0] == other[0] and pix[1] == other[1] and pix[2] == other[2]

    def get_start_pixel_list(self) -> list[Vector]:
        x_positions = []
        y_positions = []
        for i in range(0, len(self.pixels)):
            for j in range(0, len(self.pixels[i])):
                pix = self.pixels[i][j]
                if self.pix_equal(pix, Track.START_TILE):
                    x_positions.append(j)
                    y_positions.append(len(self.pixels) -1 - i)

        return [Vector(x, y) for x, y in zip(x_positions, y_positions)]

    def get_start_position(self) -> Vector:
        """
        Looks through the pixels and finds the pixels which are rgb(255, 0, 0) and finds the start point associated with them
        Returns the (x,y) position as a vector.
        """
        red_pixels = self.get_start_pixel_list()
        y_positions = [pix.y for pix in red_pixels]
        x_positions = [pix.x for pix in red_pixels]
        return Vector((min(y_positions) + max(y_positions)) / 2, (min(x_positions) + max(x_positions)) / 2)

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
            for j in range(0, len(self.pixels[i])):
                print(self.pixels[i][j])
                if self.pix_equal(self.pixels[i][j], Track.END_TILE):
                    green_pixel_list.append(Vector(j, len(self.pixels) - 1 - i))
        return green_pixel_list
        
