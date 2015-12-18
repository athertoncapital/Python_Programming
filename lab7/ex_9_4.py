import random

def arandlist():
    list2 = []
    for k in range(100):
        i2 = random.randrange(0,1001)
        list2.append(i2)
    return list2
randlist = arandlist()
print(randlist)
print("Average:", sum(randlist)/len(randlist))

