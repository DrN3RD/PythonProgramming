# Five Click House
from graphics import *
def main():

    #Window related metric
    win = GraphWin(" Five Click House", 800,800)
    win.setCoords(0.0,0.0,100,100)

    message = Text(Point(20,2), "Build a house with 5 clicks")
    message.draw(win)




    # House base
    message.setText("Click to define first point of house")

    p1 = win.getMouse()

    pt = Circle(p1,0.01).draw(win)

    message.setText("Click to define opposing corner of home")

    p2 = win.getMouse()

    # Variables
    house_base =Rectangle(p1,p2).draw(win)

    house_width = abs(p1.getX() - p2.getX())
    house_height = abs(p2.getY()- p1.getY())
    print(house_height)
    door_width = 1 / 10 * (house_width)

    message.setText("Click to set door")

    p3 = win.getMouse()
    door = Rectangle(Point(p3.getX()-(1/2)*door_width,p1.getY()),Point(p3.getX()+(1/2)*door_width, (p1.getY()+ house_height/2))).draw(win)

    message.setText("Now Set the window Position")

    p4 = win.getMouse()
    window_height = house_height/2
    window = Rectangle(Point(p4.getX()- door_width/2, p1.getY()+window_height-door_width/2 ), Point(p4.getX()+ door_width/2,p1.getY()+window_height+door_width/2 )).draw(win)

    message.setText("Now you will build the roof")

    p5 = win.getMouse()
    roof = Polygon(p2,p5,Point(p1.getX(),p2.getY())).draw(win)

    win.getMouse()

main()
