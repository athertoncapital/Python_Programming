import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jose = turtle.Turtle()
jose.color("blue")
jose.shape("turtle")
jose.penup()
for size in range(12):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(30)
wn.exitonclick()
