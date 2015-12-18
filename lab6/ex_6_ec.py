def drawSprite(n):




        import turtle

        wn = turtle.Screen()


        angle = 360 / n

        babbage = turtle.Turtle()
        babbage.shape("triangle")


        for i in range(n):
            # draw the leg
            babbage.right(angle)
            babbage.forward(120)
            babbage.stamp()
            babbage.color("red")

            # go back to the middle and turn back around
            babbage.right(180)
            babbage.forward(120)
            babbage.right(180)

        #babbage.shape("circle")
        wn.exitonclick()
def main():

    n=5
    while n!=0:

        drawSprite(n)
        n = int(input("How many legs should this sprite have?, Type '0' to quit the loop!"))

main()
