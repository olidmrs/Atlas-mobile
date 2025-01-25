from . import Track
import numpy as np



class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Car:

    UP_ANGLE = 90

    def __init__(
            self, 
            body_width: float, 
            body_length: float, 
            max_speed: int, 
            max_turn_angle: int,
            track: Track
            ) -> None:
        """
        Initializes the car.

        Parameters
        ----------
        body_width : float
            The width in centimeters of the widest point of the car (including the tires if the tires are wider than the body). 
        body_length : float
            The length in centimeters of the longest point of the car (nose to tail) 
            (including the tires if the tires contribute to the length)
        max_speed : int
            The maximum speed the car can reach. This is the real life speed of the car in cm/second.
        max_turn_angle : int
            The maximum turning angle of the front tire of the car. (The maximum angle the tire can deviate from straight forward)
        track : Track
            The track object containing the track data, and the start location.
        """
        
        # Define properties
        self.body_width = body_width
        self.body_width = body_length
        self.max_speed = max_speed
        self.max_turn_angle = max_turn_angle
        self.track = track

        # Initialize
        self.initialize()

    def _initialize(self) -> None:
        self.current_speed = 0
        self.angle = Car.UP_ANGLE
        self.positon = Vector()

    def get_state(self) -> dict:
        raise NotImplementedError()

    def drive(self, speed: float) -> None:
        self.speed = speed

    def turn(self, angle: float) -> None:
        self.front_tire_angle = angle

    def update(self) -> None:
        self.position += self.speed