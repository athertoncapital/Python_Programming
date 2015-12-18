def avgscores():
    f = open("studentdata.txt", "r")
    for aline in f:
        items = aline.split() 
        avg=sum(float(aline) for aline in items[1:])/len(items)
        print(avg)
avgscores()
