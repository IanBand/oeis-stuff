import math
import matplotlib.pyplot as plt

def main():



    #define the range of terms that will be generated here
    range_ = range(0, 2**12) 

    seq = [lpa2(i) for i in range_]

    plt.scatter(range_, seq, 0.1)

    for i in range(0, 20):
        print(str(seq[i]) + ','),
    plt.show()

    with open("b327296.txt", 'w') as outfile:
        for i in range_:
            outfile.write(str(i) + " " + str(seq[i]) + "\n")
    outfile.close()




#lpa2(n) is the largest *possible* binary palandrome (without a leading zero) from a bag of 1s and 0s

#0      0
#1      1
#10     1
#11     11
#100    1, not 010
#101    101
#110    101
#111    111
#1000   1
#1001   1001
#1010   1001
#1011   111



#1100 -> 1001
#01 -> 1
#10000 -> 1
#11100 -> 10101
def lpa2(n):

    #convert n to binary string 
    bin_str = str(bin(n))[2:]

    #count amount of 1s and 0s in the string
    zeros = bin_str.count('0')
    ones  = len(bin_str) - zeros

    if(ones == 1 or ones == 0):
        return ones

    pal = ""
    if(ones % 2 == 1):

        #start by placing a '1' in the middle of the string
        pal = '1'

        #place as many 0s around the central '1' as possible
        for i in range(0, zeros >> 1):
                pal = '0' + pal + '0'
        
    else:

        #place all 0s in the center
        for i in range(0, zeros):
            pal += '0'

    #place the remaining 1s (guaranteed to be an even amount around the palindrome, because one '1' was placed in the middle) on either side of the palindrome
    for i in range(0, ones >> 1):
        pal = '1' + pal + '1'

    #return integer value of the constructed palindrome
    return int(pal, 2)


##### OLD #####
#largest anagram that is as close as possible to a palindrome
def lpa1(n):
    #lpa1(n) is self similar on intervals of 2^n

    #convert n to binary string 
    bin_str = str(bin(n))[2:]

    #count amount of 1s and 0s in the string
    zeros = bin_str.count('0')
    ones  = len(bin_str) - zeros

    '''
    #brute force to be a palindrome
    if(ones % 2 == 1):
        ones -= 1
    '''

    #construct largest palindromic anagram from an amount of 1s and 0s
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