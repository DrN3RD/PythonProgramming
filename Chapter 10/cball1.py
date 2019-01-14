#Canonball calculations

from math import *

def main():
    angle = float(input("Enter the angle of ejection(in degrees)"))
    vel = float(input("Enter Ejection velocity (m/s)"))
    h0 = float(input("Initial Height of canonball"))
    timestep = float(input("Enter timestep (Accuracy)"))

    #Convert angle

    theta = radians(angle)

    #Initial conditions

    xpos = 0
    ypos = h0
    xvel = vel*cos(theta)
    yvel = vel*sin(theta)

#Calculations
    while ypos > 0.0:
        xpos = xpos + timestep*xvel
        yvel_1 = yvel - timestep*9.81
        ypos = ypos + timestep*(yvel+yvel_1)/2.0
        yvel = yvel_1

    print("\n Distance Travelled: {0:0.1f} meters".format(xpos))
main()