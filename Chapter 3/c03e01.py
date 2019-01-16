#Volume calculator


from math import *

def main():



    r = float(input("Enter the radius of the shpere to be calculated: "))

    volume = (4/3)*pi*(r**3)

    area = 4*pi * r**2


    print("The area of the Shpere is {0:0.1f} square meters ".format(area))
    print("\n The Volume of the sphere is {0:0.1f} cubic meters".format(volume))
    input("Enter to quit")
main()

