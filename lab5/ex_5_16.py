#pi approximation by Madhava Method
def myPi():
    I=0
    n=int(input("O hai, enter a nonzero number to tell me how many term you sum up, i.e. truncate the Madhava series to which term? (for obtain a number 3.14, it's better to enter a number larger than 700):"))
    if n>0:       
        for i in range(n):
            I=I+4*(((-1)**i)/(2*i+1))
        print(I)
    else: 
        print("nonvalid value")
    #return I
def main():
    myPi()
main()
