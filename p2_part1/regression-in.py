__author__ = 'williamchuang'
import sys
print("Please use something like: $ python3 regression-in.py labdata.txt")
if len(sys.argv) != 2:
    print("Incorrect command line arguments, please use something like:")
    print("$ python3 regression-in.py labdata.txt")
    sys.exit(1)
filename = sys.argv[1] # get the argument passed to us by operating system
data=open(str(filename),"r")


def plotRegression(data):
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    lit=[]
    x_lst=[]
    y_lst=[]
    # Set up our variables for the formula.
    for i in data:
        lit+=i.split()
        x_lst.append(float(lit[0].strip()))
        y_lst.append(float(lit[1].strip()))
        lit=[]
    print(x_lst)
    print(y_lst)

    x_sum=0
    for j in x_lst:
        x_sum+=float(j)
    x_mean=(x_sum/len(x_lst))
    y_sum=0
    for j in y_lst:
        y_sum+=float(j)
    y_mean=(y_sum/len(y_lst))
    xysum=0
    for k in range(len(x_lst)):
        xysum+=(float(x_lst[k])**2)
    xsquaresum=0
    for l in range(len(x_lst)):
        xsquaresum+=(float(x_lst[l])**2)
    m=(xysum-len(x_lst)*x_mean*y_mean)/(xsquaresum-len(x_lst)*x_mean*x_mean)
    ymin=y_mean+m*(float(min(x_lst))-x_mean)
    ymax=y_mean+m*(float(max(x_lst))-x_mean)
    print(m)

    # Get min and max values for coordinate system.
    x_min, x_max, y_min, y_max = float(min(x_lst)), float(max(x_lst)), float(min(y_lst)), float(max(y_lst))
    #print(x_min, x_max, y_min, y_max)
    # Add 10 points on each line to be safe.
    wn.setworldcoordinates(x_min-10,y_min-10,x_max+10,y_max+10)
    #t.pensize(5)
    t.up()
    for i in range(len(x_lst)):
        #t.down()
        t.setpos(float(x_lst[i]), float(y_lst[i]))
        t.dot()
        t.up()

    t.goto(float(min(x_lst)),ymin)
    t.down()
    t.goto(float(max(x_lst)),ymax)



    wn.exitonclick()


plotRegression(data)

