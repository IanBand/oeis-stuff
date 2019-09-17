import math
import matplotlib.pyplot as plt
import fractions

def main():

    r = 100000
    range_ = range(0, r) 

    seq = wanderingSum(r)
    plt.scatter(range_, seq, 5)

    plt.yscale('log')
    #plt.xscale('log')
    plt.show()

    #print(a_iter(93))

#a(n) = (a(n-1) + a(n-2))/gcd(a(n-1), a(n-2)) if gcd(a(n-1), a(n-2)) != 1
def a_recursive(n):
    #sequence seems to explode after n = 92, then again at ~4000
    if(n == 0 or n == 1):
        return 1
    a1 = a_recursive(n-1)
    a2 = a_recursive(n-2)

    gcdPrev2 = fractions.gcd(a1, a2)

    if( gcdPrev2 > 1):
        return int((a1 + a2) / gcdPrev2)

    return a1 + a2 + 1

def a_iter(n): #Iteratively generates an array of n terms, n should be greater than 2

    a1 = 0 #this will hold a(n-1), its inital value is a(1)
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

#choses the largest gcd of the prev 3 terms
def last_3_recursive(n):
    
    if(n == 0):
        return 1
    if(n == 1):
        return 2
    if(n == 2):
        return 3
    a1 = a_recursive(n-1)
    a2 = a_recursive(n-2)
    a3 = a_recursive(n-3)

    gcd12 = fractions.gcd(a1, a2)
    gcd13 = fractions.gcd(a1, a3)
    gcd23 = fractions.gcd(a2, a3)

    largestGcd = max(gcd12, gcd13, gcd23)
    

    if(gcd12 == gcd13 or gcd12 == gcd23 or gcd13 == gcd23):
        return a1 + a2 - a3 + 1

    if(largestGcd == gcd12):
        return int((a1 + a2) / gcd12) - a3

    if(largestGcd == gcd13):
        return int((a1 + a3) / gcd13) - a2

    #if(largestGcd == gcd23):
    return int((a2 + a3) / gcd23) - a1


#sum every a(n)th term
def wanderingSum(n): #generates an array of the first n terms of the series
    #allocate array
    a = [None] * n
    a[0] = 1
    a[1] = 2
    a[2] = 3

    for i in range(3, n):
        gap = a[i-1]
        s = 0
        j = 1
        while j < i:
            s += a[j]
            j = j + (gap % a[j]) + 1

        a[i] = s
    return a
if __name__ == "__main__":
    main()