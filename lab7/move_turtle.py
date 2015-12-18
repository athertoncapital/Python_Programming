__author__ = 'williamchuang'
import turtle
import re

def setup(col, x, y, w, s, shape):
    record.write("DOWN\n")
    turtle.up()
    turtle.goto(x,y)
    turtle.width(w)
    turtle.turtlesize(s)
    turtle.color(col)
    turtle.shape(shape)
    turtle.down()

    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(back, "Down")
    wn.onkey(quitTurtles, "Q")
    wn.onkey(quitTurtles, "q")
    wn.onkey(quitTurtles, "Escape")
    wn.listen()
    wn.mainloop()

#Event handlers
def up():
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.fd(5)
    record.write(str(x)+" "+str(y)+"\n")


def left():
    turtle.lt(5)
    x=turtle.xcor()
    y=turtle.ycor()
    record.write(str(x)+" "+str(y)+"\n")


def right():
    turtle.rt(5)
    x=turtle.xcor()
    y=turtle.ycor()
    record.write(str(x)+" "+str(y)+"\n")


def back():
    turtle.bk(5)
    x=turtle.xcor()
    y=turtle.ycor()
    record.write(str(x)+" "+str(y)+"\n")


def quitTurtles():
    wn.bye()
    record=open("record.txt","a")
    record.close()



wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)
record=open("record.txt","a")
setup("blue",0,0,2,2,"turtle")
