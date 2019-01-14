from graphics import *

def main():
    win = GraphWin("Clcik n Type", 800, 800)
    win.setCoords(0.0,0.0,50,50)

    message = Text(Point(10,2),"Click n Type to continue")
    message.draw(win)
    for i in range(10):
        pt = win.getMouse()
        msg = Text(Point(pt.getX()+1, pt.getY()+1),"write something")
        msg.draw(win)
        key = win.getKey()
        msg.undraw()
        label= Text(pt,key)
        label.draw(win)

main()