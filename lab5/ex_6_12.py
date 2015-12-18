from test import testEqual

def isLeap(year):
    if year%100==0:
        if year%400==0:
            return True
        else: 
            return False
    else:
        if year%4==0:
            return True
        else:
            return False    

testEqual(isLeap(1944), True)
testEqual(isLeap(2011), False)
testEqual(isLeap(1986), False)
testEqual(isLeap(1800), False)
testEqual(isLeap(1900), False)
testEqual(isLeap(2000), True)
testEqual(isLeap(2056), True)
