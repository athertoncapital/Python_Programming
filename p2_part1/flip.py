__author__ = 'William_Chuang'
import sys
from PIL import Image
# define your flip function here

def f(i):
    i2=i.copy()
    pixels = i.load() # this is not a list, nor is it list()'able
    pixels2= i2.load()
    width, height = i.size
    for x in range(width):
        for y in range(height):
            pixels[x,y]=pixels2[width-1-x,y]
            #with open('output.png','w') as f:
                #f.write(pixels[x,y]) can't write, cuz it's not str
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
