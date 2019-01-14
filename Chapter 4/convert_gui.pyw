#convert_gui.pyw

# Program to convert Celsius to Farenheit using a simple graphical interface

from graphics import *

def main():
    win = GraphWin("Celsius converter", 600,600)
    win.setCoords(0.0,0.0,3.0,4.0)

    #Draw interface

    Text(Point(1,1),"Farenheit Temperature:").draw(win)
    Text(Point(1,3), "   Celcius Temperature:").draw(win)

    inputText = Entry(Point(2.25,3),5)
    inputText.setText("0.0")

    inputText.draw(win)

    outputText = Text(Point(2.25,1)," ")
    outputText.draw(win)


    button = Text(Point(1.5,2.0), "Convert it")

    button.draw(win)
    Rectangle(Point(1,1.15),Point(2,2.5)).draw(win)

    #Wait for mouse click

    win.getMouse()

    #Continue operation

    celcius = float(inputText.getText())
    fahrenheit = 9.0/5.0 *celcius + 32

    outputText.setText(round(fahrenheit,3))
    button.setText("quit")


    win.getMouse()
    win.close()
main()