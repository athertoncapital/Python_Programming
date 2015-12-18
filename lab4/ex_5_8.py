from test import testEqual
import math
def areaOfCircle(r):
    t=r*r*math.pi
    return t   

t = areaOfCircle(0)
testEqual(t,0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(100)
testEqual(t,31415.926535897932)
