import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.right(90)
        t.forward(sz)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")
alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

x=10
y=10
sz=20
for i in range(5):
    drawSquare(alex, sz)   # Call the function to draw the square
    alex.penup()
    alex.goto(x,y)
    x=x+10
    y=y+10       # move alex to the starting position for the next square
    sz=sz+20
    alex.pendown()

    

wn.exitonclick()
