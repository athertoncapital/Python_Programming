from test import testEqual

def reverse(astring):
    j=""
    s=len(astring)
    for i in range(s):
        j=astring[i]+j
    return j
 

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")
