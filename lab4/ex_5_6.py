import turtle

def drawPoly(t, s):
    ''' takes a turtle, t, and an angle in degrees '''
    
    for i in range(3):
        t.forward(s)
        t.left(120)
#def drawEquitriangle(someturtle, somesize)     

def drawEquitriangle(size):
    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    hoho = turtle.Turtle()    # create hoho
    hoho.color('blue')

# draw the spiral using a 90 degree turn angle
    drawPoly(hoho, size)
#if __name__ == "__main__":
#    main()
drawEquitriangle(150)
