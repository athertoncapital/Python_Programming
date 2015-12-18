from test import testEqual

def findHypot(a,b):
    hypotenuse=(a**2+b**2)**0.5
    print(hypotenuse)
    return hypotenuse

testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)
