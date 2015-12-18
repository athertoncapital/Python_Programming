from test import testEqual

def is_odd(n):
    if n%2!=0:
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)
