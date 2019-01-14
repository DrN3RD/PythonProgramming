
from projectile import Projectile




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