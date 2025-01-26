import numpy as np
from .vector import Vector

class Track:
    def __init__(
            self,
            pixels : np.ndarray
    ):
        self.pixels = pixels
    
    def get_start_position(self) -> Vector:
        pass

    def get_state(self) -> np.ndarray:
        pass
    
    def get_end_position(self) -> Vector:
        pass