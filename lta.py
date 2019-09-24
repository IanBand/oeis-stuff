import math
import matplotlib.pyplot as plt

def main():



    #define the range of terms that will be generated here
    range_ = range(0, 3**10) 

    seq = [lta(i) for i in range_]

    plt.scatter(range_, seq, 0.3)

    #for i in range_:
        #print(str(seq[i]) + ','),
        #lta(i)


    plt.show()

    #with open("lta.txt", 'w') as outfile:
    #    for i in range_:
    #        outfile.write(str(i) + " " + str(seq[i]) + "\n")
    #outfile.close()

def lta(n):
    '''
    examples:
    200 -> 2
    202 -> 202
    102 -> 2
    110022 -> 210012
    111000222 -> 2102012
    '''
    tri_str = base10toN(n,3)

    #count numerals
    zeros = tri_str.count('0')
    ones  = tri_str.count('1')
    twos  = tri_str.count('2')

    pal = ""

    #determine if a digit should be placed in the middle of the palindrome
    if(twos % 2 == 1): #if there are an odd number of 2's, place a 2 in the middle of the palindrome
        pal = "2"
        twos -= 1
    elif(ones % 2 == 1):
        pal = "1"
        ones -= 1
    elif(zeros % 2 == 1):
        pal = "0"
        zeros -= 1

    #place remaining digits around the center of the palindrome

    #if there are enough 1's or 2's to cap the ends of the palindrome (since the palindrome cannot have leading zeros)
    if(ones >= 2 or twos >= 2): 
        #place remaining 0's on either side of the palindrome
        while zeros - 2 >= 0:
            pal = "0" + pal + "0" 
            zeros -= 2
    
    #place remaining 1's on either side of the palindrome
    while ones - 2 >= 0:
        pal = "1" + pal + "1"
        ones -= 2

    #place remaining 2's on either side of the palindrome
    while twos - 2 >= 0:
        pal = "2" + pal + "2"
        twos -= 2

    #print(pal + "\t   " + tri_str)
    return int(pal, 3)

def base10toN(num, base): #http://code.activestate.com/recipes/577586-converts-from-decimal-to-any-base-between-2-and-26/
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

numerals_ = "0123456789abcdefghijklmnopqrstuvwxyz"

#https://stackoverflow.com/a/2267428
def baseN(num,b,numerals=numerals_):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def largestBaseNPalindrome(n,b, numerals=numerals_):
    baseN_str = baseN(n,b, numerals)

    #count numerals
    numeralCount = []
    for i in range(0,b):
        numeralCount[i] = baseN_str.count(numerals[i])

    pal = ""

    #determine if a digit should be placed in the middle of the palindrome
    for i in range(0,b):
        if numeralCount[i] % 2 == 1:
            pal = numerals[i]
            numeralCount[i] -= 1
            break

    #place remaining digits around the center of the palindrome, does NOT check for leading zeros...
    for i in range(0,b):
        while numeralCount[i] >= 2:
            pal = numeral[i] + pal + numeral[i]
            numeralCount[i] -= 2
    
    return int(pal, b)
if __name__ == "__main__":
    main()