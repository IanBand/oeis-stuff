#a(n) = (a(n-1) + a(n-2))/gcd(a(n-1), a(n-2)) if gcd(a(n-1), a(n-2)) != 1


import math
import matplotlib.pyplot as plt
import fractions

def main():

    r = 700#sequence seems to explode after n = 92, then again at ~4000
    range_ = range(0, r) 

    seq = a_iter(r)
    plt.scatter(range_, seq, 5)

    plt.yscale('log')
    #plt.xscale('log')
    plt.show()

    #print(a_iter(93))



def a_recursive(n):
    
    if(n == 0 or n == 1):
        return 1
    a1 = a_recursive(n-1)
    a2 = a_recursive(n-2)

    gcdPrev2 = fractions.gcd(a1, a2)

    if( gcdPrev2 > 1):
        return int((a1 + a2) / gcdPrev2)

    return a1 + a2 + 1

def a_iter(n): #Iteratively generates an array of n terms, n should be greater than 2

    a1 = 1 #this will hold a(n-1), its inital value is a(1)
    a2 = 1 #this will hold a(n-2), its inital value is a(0)

    #allocate array
    terms = [None] * n
    terms[0] = a2
    terms[1] = a1

    for i in range(2, n):
        gcdPrev2 = fractions.gcd(a1, a2)

        if(gcdPrev2 > 1):
            terms[i] = int((a1 + a2) / gcdPrev2)

        else:
            terms[i] = a1 + a2 + 1

        a2 = a1
        a1 = terms[i]

    return terms


if __name__ == "__main__":
    main()