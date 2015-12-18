import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)
def drawFivePointStar2(t):
    for i in range(5):
        t.forward(10)
        t.left(216)        

wolfram = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wolfram.color('hotpink')
wolfram.pensize(3)
wolfram.penup()
wolfram.goto(-190,50)
for i in range(5):
    wolfram.pendown()
    drawFivePointStar(wolfram)
    wolfram.penup()
    wolfram.forward(350)
    wolfram.right(144)
    
wn2 = turtle.Screen()
wolfram2 = turtle.Turtle()
wn2.bgcolor("lightgreen")
wolfram2.color('red')
wolfram2.pensize(3)
wolfram2.penup()
wolfram2.goto(120,150)
for i in range(5):
    wolfram2.pendown()
    drawFivePointStar2(wolfram2)
    #wolfram.penup()
    wolfram2.forward(35.0)
    wolfram2.right(144)
print("If line 19 be ignore, i.e. didn't pickup the pen, then it would look like the figure, wolfram2, on the upper right, which is a 10:1 size picture. It shows that the five small star will be located at the five angles of the larger star with 350:100 ratio on their sides.")
