from test import testEqual

def is_rightangled(a, b, c):
    x=(a**2+b**2)**0.5
    y=c
    if  abs(x - y) < 0.00001:      # if x is approximately equal to y
        return True
    else:
        return False

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)
