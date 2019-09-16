import math
import matplotlib.pyplot as plt

numerals_ = "0123456789abcdefghijklmnopqrstuvwxyz"

def main():

    #define the range of terms that will be generated here
    range_ = range(0, 1000) 

    seq = [prodOcc2(i) for i in range_]

    plt.scatter(range_, seq, 0.5)

    for i in range(0, 20):
        print(str(seq[i]) + ", "),
    plt.show()

#product of the occurences of the digits in n, base 2, includes zero occurances in product
def prodOcc2(n):
    #convert n to binary string 
    bin_str = str(bin(n))[2:]

    #count amount of 1s and 0s in the string
    zeros = bin_str.count('0')
    ones  = len(bin_str) - zeros

    return ones * zeros


#https://stackoverflow.com/a/2267428
def baseN(num,b,numerals=numerals_):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

#returns the product of the occurances of all digits of a number in a specified base. including zero occurances in the product is optional
def prodOcc(n, base, numerals=numerals_, incZerosInProd=False):

    num_str = baseN(n, base, numerals)
    product = 1

    for i in range(0, base):
        occ = num_str.count(numerals[i])
        if(occ > 1 or incZerosInProd): #this condition is optional, and changes the product a lot
            product *= occ

    return product
        




if __name__ == "__main__":
    main()