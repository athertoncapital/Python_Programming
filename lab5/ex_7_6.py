import random
import turtle

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0 and abs(t.xcor())+16<wn.window_width() / 2 and abs(t.ycor())+16<wn.window_height() / 2:
        t.left(90)
    else:
        t.right(90)
        if abs(t.xcor())+16<wn.window_width() / 2 and abs(t.ycor())+16<wn.window_height() / 2:
            t.forward(10)
        else:
            t.left(180)
            t.forward(10)


def areColliding(t1, t2):
    if t1.distance(t2) > 10:
        return True
    else:
        t1.left(180)
        t2.right(180)
        return True

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = True
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = True
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

t1.up()
t1.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while isInScreen(wn, t1) and isInScreen(wn, t2):
    while areColliding(t1, t2):
        moveRandom(wn, t1)
        moveRandom(wn, t2)

wn.exitonclick()
