import math
import matplotlib.pyplot as plt

def main():
    
    #define the range of terms that will be generated here

    range_ = range(0, 2**16) #largePalAna(n) is self simmilar on intervals of 2^n

    seq = [largePalAna(i) for i in range_]

    plt.scatter(range_, seq, 0.1)

    plt.show()

#largest palindromic anagram
def largePalAna(n):

    #convert n to binary string 
    bin_str = str(bin(n))[2:]

    #count ammount of 1s and 0s in the string
    zeros = bin_str.count('0')
    ones  = len(bin_str) - zeros

    #construct largest palindromic anagram from an ammount of 1s and 0s
    pal = ""

    #place all 0s in the middle of the string
    for i in range(0, zeros):
        pal += '0'
    
    #alternate placing the remaining 1s on either end of the string
    for i in range(0, ones):

        #if even, append '1' to left (msb)
        if(i % 2 == 0):
            pal = '1' + pal

        #else append 1 to right (lsb)
        else:
            pal += '1'

    #return integer value of the constructed palindrome
    return int(pal, 2)

if __name__ == "__main__":
    main()