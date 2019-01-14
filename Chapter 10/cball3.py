
from math import *


class Projectile:
    def __init__(self,angle,velocity,height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)

    def update(self,timestep):

        self.xpos = self.xpos + timestep* self.xvel
        self.yvel_1 = self.yvel -9.81*timestep

        self.ypos = self.ypos + timestep*(self.yvel + self.yvel_1)/2
        self.yvel = self.yvel_1

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

def getInputs():

    a = float(input("Enter degree angle"))
    v = float(input("Enter velocity"))
    h = float(input("Enter initial height"))
    t = float((input("enter timestep")))

    return  a,v,h,t

def main():
    angle,vel,h0,timestep = getInputs()

    cball = Projectile(angle,vel,h0)

    while cball.getY() >= 0:
        cball.update(timestep)
    print("Distance travelled is ", cball.getX(),"meters")

    print("Distance traveled is {0:0.1f} meters".format(cball.getX()))

main()