import sys
from PIL import Image
# define your flip function here

def median(list):
    x=sorted(list)
    #print(x[len(x)//2])
    #return x[len(x)//2]
    length = len(x)
    sorts = sorted(x)

    if length % 2==0:
        #print((sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0)
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    else:
        #print(sorts[int(length / 2)])
        return sorts[int(length / 2)]
def getpixel(i,x,y):
    width,height = i.size
    pixel=i.load()
    if x<0:
        if y<0:
            return pixel[0,0]
        elif y>=height:
            return pixel[0,height-1]
        else:
            return pixel[0,y]
    elif x>=width:
        if y<0:
            return pixel[width-1,0]
        elif y>=height:
            return pixel[width-1,height-1]
        else:
            return pixel[width-1,y]
    else:
        if y<0:
            return pixel[x,0]
        elif y>=height:
            return pixel[x,height-1]
        else:
            return pixel[x,y]
def f(i):
    #i2=i.copy()
    pixels = i.load() # this is not a list, nor is it list()'able
    #pixels2= i2.load()
    width, height = i.size
    for x in range(0,width,1):
        for y in range(0,height,1):
            p1=getpixel(i,x-1,y+1)
            p2=getpixel(i,x,y+1)
            p3=getpixel(i,x+1,y+1)
            p4=getpixel(i,x-1,y)
            p5=getpixel(i,x,y)
            p6=getpixel(i,x+1,y)
            p7=getpixel(i,x-1,y-1)
            p8=getpixel(i,x,y-1)
            p9=getpixel(i,x+1,y-1)
            ##################################Only targeting to black, white, and have a large difference with nbhd pixels#####################
            #if (p1+p2+p3+p4+p6+p7+p8+p9)/8>250:
            #    pblur=median([p1,p2,p3,p4,p5,p6,p7,p8,p9])
            #    pixels[x,y]=pblur
            #elif (p1+p2+p3+p4+p6+p7+p8+p9)/8<10:
            #    pblur=median([p1,p2,p3,p4,p5,p6,p7,p8,p9])
            #    pixels[x,y]=pblur
            #elif (pixels[x,y]-median([p1,p2,p3,p4,p5,p6,p7,p8,p9]))>50:
            #    pblur=median([p1,p2,p3,p4,p5,p6,p7,p8,p9])
            #    pixels[x,y]=pblur
            #elif (pixels[x,y]-median([p1,p2,p3,p4,p5,p6,p7,p8,p9]))<-50:
            #    pblur=median([p1,p2,p3,p4,p5,p6,p7,p8,p9])
            #    pixels[x,y]=pblur
            #else:
            #    pixels[x,y]=pixels[x,y]
            #################################the above idea can reserve more original information############################################
            pblur=median([p1,p2,p3,p4,p5,p6,p7,p8,p9])
            pixels[x,y]=pblur

    i.save("output.png")
    i.show()

def main():
    if len(sys.argv)<=1:
            print("missing image filename")
            sys.exit(1)
    filename = sys.argv[1]
    i = Image.open(filename)
    i = i.convert("L")
    #i.show()
    #i = Image.open("obama.png")
    i=f(i)
    return i

main()
