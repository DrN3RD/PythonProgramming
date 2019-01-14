#coinToss.py

#Simulation of cointoss driven movement.
#Author: Hugo Danielson

from random import random

#Introduction print routine

def main():
    intro()
    input(" \n Press Enter to continue")

    n_simulations = get_inputs() #Gets the number of simulationw

    distance = (simNtoss(n_simulations))

    result(n_simulations,distance)

    input("Press to quit")

def intro():
    print("This simulation takes n coin tosses, and makes the player walk"
          " either forward or back depending on outcome\n")

    print("Heads leads to a positive x movement, tails does the reverse.\n"
          "Results are presented as a distance from start point. ")


def get_inputs():

    n = int(input("How many simulations do you want to run? ",))

    return n


def simNtoss(n):

    position = 0

    for i in range(n):

        simOnetoss()

        if simOnetoss()=="heads":

            position = position + 1

        else:
            position = position -1

        return position


def simOnetoss():

    prob = random()


    if prob > 0.5:
        return "heads"

    else:
        pass

def result(n,distance):

    print("After ",n,"simulations, the distance from your starting point, is a whopping", distance, "steps")




if __name__ == '__main__': main()
