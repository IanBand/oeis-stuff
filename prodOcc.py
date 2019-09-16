import math
import matplotlib.pyplot as plt

def main():

    #define the range of terms that will be generated here
    range_ = range(0, 1000) 

    seq = [prodOcc2(i) for i in range_]

    plt.scatter(range_, seq, 0.5)

    for i in range(0, 20):
        print(str(seq[i]) + ','),
    plt.show()

#product of the occurences of the digits in n, base 2
def prodOcc2(n):
    #convert n to binary string 
    bin_str = str(bin(n))[2:]

    #count amount of 1s and 0s in the string
    zeros = bin_str.count('0')
    ones  = len(bin_str) - zeros

    return ones * zeros



if __name__ == "__main__":
    main()