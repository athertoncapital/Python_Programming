import math
print("This pi-value is given by python 3:", '%.16f' % math.pi)
print("The following results are using N sides polygon to approximate a circle and compute the pi value")
def poly(n):
    
    els = 2.0
    s = 4
    for x in range(n):
        els = 2 - 2 * math.sqrt(1 - els / 4)
        s *= 2
    return s * math.sqrt(els) / 2

def main():
    
    for n in range(16):
        r = poly(n)
        e = r - math.pi
        print("%8d iterations %.16f error %.16f" % (n, r, e))

if __name__ == "__main__":
    main()
#The if __name__ == '__main__' clause would make it run main() only if the script is executed directly


print("Observation: After iterating 13 times, we can see that the estimate of pi starts getting worse. This could cause by all the calculations are based on python's floating point number digit limit, about 16 digits, therefore all those errors accumulate and contribute to the results.")
