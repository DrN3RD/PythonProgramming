#Lets Make dat winter scene


from graphics import *


def main():

    win = GraphWin("Christmas time is here", 600,600)
    win.setCoords(0.0,0.0,200,200)

    def snowman():
        # Draw top cirlce
        col = "white"
        sn = win.getMouse()
        head = Circle(sn, 10).draw(win)
        head.setFill(col)
        head.setOutline(col)

        Leye = Circle(sn,1).draw(win)
        Leye.setFill("black")
        Leye.move(-5,2)
        Reye = Leye.clone().draw(win)
        Reye.move(10,0)

        body = Circle(sn, 25).draw(win)
        body.move(0,-30)
        body.setOutline(col)
        body.setFill(col)



    snowman()















    win.getMouse()
    win.close()
main()
