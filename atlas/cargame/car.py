from . import Track
from vector import Vector
import numpy as np
import math



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
            timestep: float,
            front_tire_relative_position: Vector,
            back_right_tire_relative_position: Vector
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
        front_tire_relative_position: Vector
            The front tire position relative to the absolute center of the car (in cm).
        back_right_tire_relative_position: Vector
            The right back tire position relative to the absolute center of the car (in cm).
        """
        
        # Define properties
        self.body_width = body_width
        self.body_length = body_length
        self.max_speed = max_speed
        self.max_tire_angle = max_tire_angle
        self.track = track
        self.timestep = timestep
        self.front_right_tire_position = front_tire_relative_position
        self.back_right_tire_position = back_right_tire_relative_position
        self.back_left_tire_position = self.back_right_tire_position.copy()
        self.wheelebase = front_tire_relative_position.y - back_right_tire_relative_position.y

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
            'CarAngle': self.angle / 360,
            'TireAngle': self.tire_angle / self.max_tire_angle
        }

    def set_speed(self, speed: float) -> None:
        """
        Sets the current speed of the car.

        Parameters
        ----------
        speed : float
            A float between 0 and 1 to indicate how fast the back tires should spin. 
            0 is stopped, 1 is the fastest they can possibly spin.
        """

        self.speed = speed * self.max_speed

    def set_front_tire_angle(self, angle: float) -> None:
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

        # Calculate the turning radius
        turning_radius = abs(self.wheelebase / math.tan(math.radians(self.front_tire_angle)))

        # Calculate Instantaneous Center of Rotation (ICR)
        center_of_back_wheels = (self.back_left_tire_position + self.back_right_tire_position) / 2

        # If tire angle is positive, subtract 180 and add the absolute value of angle
        if self.tire_angle > 0:
            angle_facing_center_of_rotation = self.angle - (Car.MAX_CAR_ANGLE / 2) + self.tire_angle
        # If tire angle is negative, add 180 and subtract absolute value of angle
        else:
            angle_facing_center_of_rotation = self.angle + (Car.MAX_CAR_ANGLE / 2) + self.tire_angle 

        # Find the offset from the car where the center of rotation should be
        offset = Vector(
            math.cos(angle_facing_center_of_rotation) * turning_radius,
            math.sin(angle_facing_center_of_rotation) * turning_radius
        )

        # Draw a circle from the center of rotation, find the potition which is speed * timestep
        position_on_circle_in_degrees = math.degrees(math.atan2(
            -offset.y,
            -offset.x
            ))
        
        # Find the difference between the current angle and the angle on the circle we should be at after driving
        angle_difference = math.degrees((self.speed * self.timestep) / turning_radius)
        # If he's turning right, subtract the angle instead of adding
        if self.tire_angle > 0:
            angle_difference *= -1

        new_position_on_circle_in_degrees = position_on_circle_in_degrees + angle_difference
        position_offset_from_circle_center_to_back_tires = Vector(
            turning_radius * math.cos(math.radians(new_position_on_circle_in_degrees)),
            turning_radius * math.sin(math.radians(new_position_on_circle_in_degrees))
            )
        
        circle_center = center_of_back_wheels + offset
        new_back_tire_positon = circle_center + position_offset_from_circle_center_to_back_tires
        
        # Calculate the new car angle
        parallel_line_angle = new_position_on_circle_in_degrees + 90
        # If car is turning to the right, subtract 180 from the angle (trust me it should work)
        if self.tire_angle > 0:
            parallel_line_angle -= 180

        self.angle = parallel_line_angle
        while self.angle >= 360:
            self.angle -= 360

        # Get direction of x-axis for the car's facing direction
        if self.angle < 180:
            if self.tire_angle < 0:
                x_direction = -1
            else:
                x_direction = 1
        else:
            if self.tire_angle < 0:
                x_direction = 1
            else:
                x_direction = -1

        # Get direction of y-axis for the car's facing direction
        if self.angle > 90 and self.angle < 270:
            if self.tire_angle < 0:
                y_direction = -1
            else:
                y_direction = 1
        else:
            if self.tire_angle < 0:
                y_direction = 1
            else:
                y_direction = -1

        slope_of_car = math.tan(math.radians(parallel_line_angle))
        x_diff = (self.body_length / 2) / math.sqrt(slope_of_car ** 2 + 1)
        y_diff = abs(slope_of_car * x_diff) 

        x_diff = x_diff * x_direction
        y_diff = y_diff * y_direction

        self.position = new_back_tire_positon +  Vector(x_diff, y_diff)

        self.reward -= 1

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
        pixels = self.track.pixels

    
    def _is_overlapping_with_end_mark(self) -> bool:
        pixels = self.track.pixels
