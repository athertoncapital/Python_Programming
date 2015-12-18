__author__ = 'Williamchuang'
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)
t.color("blue")
t.turtlesize(2)
t.shape("turtle")
f = open("record.txt", "r")

for aline in f:
    items = aline.split()
    if items[0] == "UP":
        t.up()
    else:
        if items[0] == "DOWN":
            t.down()
        else:
            # must be coords
            t.goto(float(items[0]), float(items[1]))

f.close()
wn.exitonclick()
