# projectile.py

"""projectile.py
    Provides a simple class for modeling the flight of projectiles"""

from math import *

class Projectile:

    def __init__(self,angle,velocity,height):
        """Create a projectile with given launch angle, initial velocity, and height"""

        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)

    def update(self,time):
        """Update the state of the projectile to move it according to calculation accuracy"""

        self.xpos = self.xpos + time*self.xvel
        yvel1 = self.yvel -9.81 *time
        self.ypos = self.ypos + time*(self.yvel+yvel1)/2
        self.yvel = yvel1

    def getY(self):
        """Returns the y position(height) of this projectile"""

        return self.ypos

    def getX(self):

        """Returns the x position ( distance) of the projctile"""

        return self.xpos

