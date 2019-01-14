from graphics import *

def main():
    win = GraphWin("Draw a Triangle",800,800)
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5), " Click on three points please")
    message.draw(win)

#Get three mouse clicks
    p1 = win.getMouse()
    p1 .draw(win)

    p2 = win.getMouse()
    p2 .draw(win)

    p3 = win.getMouse()
    p3 .draw(win)

#Use polygon object to draw a triangle

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    message.setText("click anywhere to quit")
    win.getMouse()
main()