from graphics import *

def handleKey(key,win):

    if key == "r":
        win.setBackground("red")

    elif key == "b":
        win.setBackground("blue")

def handleClick(pt,win):
    pass


def main():

    win = GraphWin("Color window",500,500)
    # Event loop that handles key input to change color of window


    while True:
        key = win.checkKey()

        if key == "q":
            break

        if key:
            handleKey(key,win)
        pt = win.checkMouse()

        if pt:
            handleClick(pt,win)


    win.close()
main()
