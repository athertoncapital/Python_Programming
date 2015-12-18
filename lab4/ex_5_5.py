import turtle

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2

def main():
    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    hoho = turtle.Turtle()    # create hoho
    hoho.color('blue')

## draw the first spiral ##
# position hoho
    hoho.penup()
    hoho.backward(110)
    hoho.pendown()

# draw the spiral using a 90 degree turn angle
    angle=90
    drawSpiral(hoho, 90)


## draw the second spiral ##
# position hoho
    hoho.home()
    hoho.penup()
    hoho.forward(90)
    hoho.pendown()

    drawSpiral(hoho, 89)
if __name__ == "__main__":
    main()
