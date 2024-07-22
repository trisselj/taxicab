# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Translates the motion of a taxicab on a 2D plane and measures total distance travelled

# Defining class as taxicab
class taxicab:

    # Initializes taxicab object with x,y coordinates and measurable odometer set to 0 intitially
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    # Returns x-coordinate of taxicab
    def get_x_coord(self):
        return self._x_coord

    # Returns y-coordinate of taxicab
    def get_y_coord(self):
        return self._y_coord
    
    # Returns odometer value of taxicab
    def get_odometer(self):
        return self._odometer
    
    # Moves the taxicab along the x-axis and measures distance travelled via odometer
    def move_x(self, distance):
        self._x_coord += distance
        self._odometer += abs(distance)
    
    # Moves the taxicab along the y-axis and measures distance travelled via odometer
    def move_y(self, distance):
        self._y_coord += distance
        self._odometer += abs(distance)

