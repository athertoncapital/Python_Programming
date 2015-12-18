import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
        

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")
alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

sz=60
for i in range(20):
    drawSquare(alex, sz)   # Call the function to draw the square
    alex.left(18)

wn.exitonclick()
