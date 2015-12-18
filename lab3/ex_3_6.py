import turtle
wn = turtle.Screen()
xpoly = turtle.Turtle()
xpoly.begin_fill()
c = raw_input("Enter the color you would like for edges (blue, red, yellow, purple): ")
fc= raw_input("Enter the color you would like to fill in: ")

s = int(input("Enter how many sides you would like to have: "))
xpoly.color(c)
xpoly.fillcolor(fc)
xpoly.begin_fill()
for i in range(s):    
    xpoly.forward(100)
    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    xpoly.left(360/s)
xpoly.end_fill() 
wn.exitonclick()
