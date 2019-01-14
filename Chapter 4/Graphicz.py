# This program will take the principal from user, and present netted values grphically

from graphics import *
print("This program will calculate a 10 year investment return plan")

def main():

    principal = 2000
    apr = 0.2
# Create the window properties

    win = GraphWin("Investment Growth Chart", 320*2, 240*2)
    win.setCoords(-2,-200,12,11000.0)
    win.setBackground("white")
    Text(Point(-1,1),'0.0K').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    #draw initial
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
# Draw Bars n shit
    for year in range(1,11):

        principal = principal * (1+apr)

        x11 = year * 25 + 40
        height = principal*0.02
        bar = Rectangle(Point(year,0),Point(year+1,principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("press enter to quit")
    win.close()
main()

