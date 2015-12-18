N = 12
P = 10000
x = 0.08

y = int(input("Compound for how many years? "))

result = P * ( ((1 + (x/N)) ** (y*N)) )

print ("The final amount after", y, "years is", result)

