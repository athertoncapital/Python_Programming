from test import testEqual

def count(substr,theStr):    
    i=0
    j=0
    not_found_yet=True  
    while not_found_yet:
        k = theStr.find(substr,i) 
                                
        if k==-1:         
            not_found_yet=False
        else:             
            j+=1        
            i=k+1
    print(j)
    return j
testEqual(count('is', 'Mississippi'), 2)
testEqual(count('an', 'banana'), 2)
testEqual(count('ana', 'banana'), 2)
testEqual(count('nana', 'banana'), 1)
testEqual(count('nanan', 'banana'), 0)
testEqual(count('aaa', 'aaaaaa'), 4)
