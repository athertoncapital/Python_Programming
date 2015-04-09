#Write a program, move_turtle.py, that allows the user to move the turtle with the keyboard arrow keys. 
#Record the path taken using a list. Once the user presses the Q key, save the list as a file in the same 
#format as Exercise 5 of Ch 10. You should be able to use the code in the exercise file to play back what 
#the user created (as described in Ex 5)

import turtle
import re

wn = turtle.Screen()

def setup(col, x, y, w, s, shape):
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
    keys=""
    turtle.fd(45)

    record=open("record.txt","a")
    keys = keys+"up"
    record.write(keys + '\n')
    #keys = ""
    #p=turtle.position()
    #pc=str(p)
    #keys= keys+str(pc)
    #record.write(keys + '\n')

def left():
    keys=""
    turtle.lt(45)
    record=open("record.txt","a")
    keys = keys+"left"
    record.write(keys + '\n')


def right():
    keys=""
    turtle.rt(45)
    record=open("record.txt","a")
    keys = keys+"right"
    record.write(keys + '\n')


def back():
    keys=""
    turtle.bk(45)
    record=open("record.txt","a")
    keys = keys+"back"
    record.write(keys + '\n')


def quitTurtles():
    wn.bye()
    record=open("record.txt","a")
    record.close()
setup("blue",0,0,2,2,"turtle")

