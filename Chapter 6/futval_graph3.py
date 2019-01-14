#LEarning how to use functions to simply programming



from graphics import * #Start by importing packages relevant to project

def drawBar(window,year,height):
    #Draw a bar in window starting at year with given height
    bar = Rectangle(Point(year,0),Point(year +1,height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    #Main routine
    print("This program plots the growth of a 10 year investment")

    #Get principal investment

    principal = float(input("How much do you want to invest, sir?: "))
    apr = float(input("enter the anual rate"))

    #create the graphixzzz

    win = GraphWin("Investment growth Chart",600,600)
    win.setCoords(-1.75,-200,11.5,10400)
    win.setBackground("white")

    Text(Point(-1,0),"0.0k").draw(win)

    Text(Point(-1,2500),"2.5k").draw(win)

    Text(Point(-1,5000),"5.0k").draw(win)

    Text(Point(-1,7500),"7.5.0k").draw(win)

    Text(Point(-1,10000),"10.0k").draw(win)

    drawBar(win,0,principal)

    for year in range(1,11):
        principal = principal *(1+apr)
        drawBar(win,year,principal)

    input("Press enter to quit")

    win.close()
main()