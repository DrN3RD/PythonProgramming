#Circle Mover

from graphics import *

def main():
    win = GraphWin("Draw Circles My friend", 600,600)
    win.setCoords(0,0,100,100)
    shape = Circle(Point(50,50),5)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse() #Where you want the shape to go to
        c = shape.getCenter() #Gets the coordinates of the circle centre for further calc
        dx = p.getX()-c.getX() #Calc x difference from drawn to desired
        dy = p.getY()-c.getY() #calc y, same as above
        shape.move(dx,dy) #moves it
    win.close()
main()
