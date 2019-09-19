import sys
import json

def main():
    #check for input files
    if(len(sys.argv) != 3):
        print("error, please provide two input file names")
        return
    print("comparing datasets: " + sys.argv[1] + " and " + sys.argv[2])

    array1 = json.load(open(sys.argv[1]))
    array2 = json.load(open(sys.argv[2]))

    numTerms = len(array2)

    if len(array1) < len(array2):
        numTerms = len(array1)

    print("comparing " + str(numTerms) + " terms")

    for i in range(numTerms):
        if array1[i] != array2[i]:
            print("the datasets differ on term " + str(i))
            print(sys.argv[1] + "has the value " + str(array1[i]))
            print(sys.argv[2] + "has the value " + str(array2[i]))
            break
    print('data sets are equal!')



if __name__ == "__main__":
    main()