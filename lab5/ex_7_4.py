import random
import turtle

def moveRandom(wn, t):
    angle = random.randrange(0,360)
    t.left(angle)
    t.forward(50)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn
def main():
    t1 = turtle.Turtle()
    wn = turtle.Screen()
    t1.shape('turtle')
    leftBound = -wn.window_width() / 2
    rightBound = wn.window_width() / 2
    topBound = wn.window_height() / 2
    bottomBound = -wn.window_height() / 2

    t1.up()
    t1.goto(random.randrange(leftBound, rightBound),
    random.randrange(bottomBound, topBound))
    t1.setheading(random.randrange(0, 360))
    t1.down()


    while isInScreen(wn, t1):
        moveRandom(wn, t1)

    wn.exitonclick()
main()
