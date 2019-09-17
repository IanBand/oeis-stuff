#Numbers n such that the average of the digits (in base 10) of n is an integer
import math
import matplotlib.pyplot as plt

numerals_ = "0123456789abcdefghijklmnopqrstuvwxyz"

def main():

    #define the range of terms that will be checked here
    range_ = range(0, 1000) 

    #seq = [prodOcc2(i) for i in range_]

    #plt.scatter(range_, seq, 0.5)

    #for i in range(0, 20):
    #    print(str(seq[i]) + ", "),
    #plt.show()

#https://stackoverflow.com/a/2267428
def baseN(num,b,numerals=numerals_):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

#returns the product of the occurances of all digits of a number in a specified base. including zero occurances in the product is optional
def intAvgDiv(n, base, numerals=numerals_):

        numStr = baseN(n, base, numerals);

        math.gcd()




if __name__ == "__main__":
    main()