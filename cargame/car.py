from . import Track
from vector import Vector
import numpy as np



class Car:

    UP_ANGLE = 90
    MAX_CAR_ANGLE = 360
    START_REWARD = 360

    def __init__(
            self, 
            body_width: float, 
            body_length: float, 
            max_speed: int, 
            max_tire_angle: int,
            track: Track,
            timestep: float
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
        max_tire_angle : int
            The maximum turning angle of the front tire of the car. (The maximum angle the tire can deviate from straight forward)
        track : Track
            The track object containing the track data, and the start location.
        timestep: float
            The number of seconds between each update.
        """
        
        # Define properties
        self.body_width = body_width
        self.body_width = body_length
        self.max_speed = max_speed
        self.max_tire_angle = max_tire_angle
        self.track = track
        self.timestep = timestep

        # Initialize
        self._initialize()

    def _initialize(self) -> None:
        self.speed = 0
        self.positon = self.track.start_position
        self.angle = Car.UP_ANGLE
        self.tire_angle = 0
        self.reward = Car.START_REWARD

    def get_state(self) -> dict:
        """
        Gets the current state of the car.

        Returns
        -------
        dict
            Returns the following dictionary:
            {
                'Grid': np.ndarray,
                'CarPosition': np.ndarray # [x: float, y: float]
                'CarSpeed': float,
                'CarAngle': float,
                'TireAngle': float
            }
        """
        return {
            'Grid': self.track.get_state(),
            'CarPosition': np.ndarray([self.position.x, self.position.y]),
            'CarSpeed': self.speed,
            'CarAngle': self.angle / ,
            'TireAngle': self.tire_angle / self.max_tire_angle
        }

    def drive(self, speed: float) -> None:
        """
        Sets the current speed of the car.

        Parameters
        ----------
        speed : float
            A float between 0 and 1 to indicate how fast the back tires should spin. 
            0 is stopped, 1 is the fastest they can possibly spin.
        """

        self.speed = speed * self.max_speed

    def turn(self, angle: float) -> None:
        """
        Sets the angle of the car to some angle between -max_tire_angle and max_tire_angle

        Parameters
        ----------
        angle : float
            A float between -1 and 0, which will be mapped to the maximum turn angle.
        """
        self.front_tire_angle = angle * self.max_tire_angle

    def update(self) -> None:
        """
        Updates the angle and position based on the current speed and tire angle. The position and car angle at the end
        of this method is the position and angle the car would be in after one timestep elapsing with the current tire angle
        and speed. For example, if the speed is 10cm/sec and the car angle is 90 (straight up) and the timestep is 1 second,
        the car will be 10cm straight up at the end of this function.
        """

        self.reward -= 1
        # TODO: Update the position and the angle of the car given the current tire angle and speed
        raise NotImplementedError()

    def reset(self) -> None:
        """
        Resets the car back to the initial position and state.
        """
        self._initialize()

    def get_reward(self) -> None:
        return self.reward
    
    def check_if_terminated(self) -> bool:
        return self._is_in_track()
    
    def check_if_done(self) -> bool:
        return self._is_overlapping_with_end_mark()
    
    def _is_in_track(self) -> bool:
        raise NotImplementedError()
    
    def _is_overlapping_with_end_mark() -> bool:
        raise NotImplementedError()
