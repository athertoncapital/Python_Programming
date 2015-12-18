from test import testEqual

def remove_letter(theLetter, theString):
    s=len(theString)
    j=""
    for i in theString:
        if i!=theLetter:
            j=j+i    
    return j

testEqual(remove_letter('a', 'apple'), 'pple')
testEqual(remove_letter('a', 'banana'), 'bnn')
testEqual(remove_letter('z', 'banana'), 'banana')
