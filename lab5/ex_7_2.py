def print_triangular_numbers(n):
    
    n=int(input("O hai, enter a nonzero number to tell me how many term you want:"))
    if n>0:
        for i in range(1,n+1,1):
            T=(i*(i+1))/2
            print(i, '\t', T)
    else: 
        print("nonvalid value")
    #return I
def main(n):
    print_triangular_numbers(n)
main(5)
