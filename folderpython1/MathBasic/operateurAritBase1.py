import sys
from math import ceil


def getMaxBytesFromInt():
    maxSizeInt = sys.maxsize
    print("Max Bytes of int is " + str(maxSizeInt))
    print("Max Bytes of int is " + str(getBytesFromInt(maxSizeInt)))


def getBytesFromInt(number):
    sizeInt = ceil(number.bit_length() / 8.0)
    print("Bytes of int=" + str(number) + " is " + str(sizeInt))
    return sizeInt


# masque pour representer la partie Byte(8 premières bits)
# d'un entier int (number1)
def calculateByteEquivalent(number1, number2):
    byte_number1 = number1 & 0xFF;
    byte_number2 = number2 & 0xFF;
    return [byte_number1, byte_number2]


def Main():
    numbers = calculateByteEquivalent(255, 257)
    print("the value of unit is =" + str(numbers[0]))
    print("the value of diz is =" + str(numbers[1]))

    getBytesFromInt(256)
    getBytesFromInt(255)
    getBytesFromInt(9223372036854775807)
    getBytesFromInt(0b00001111)
    getBytesFromInt(92233720368597758099)

    getMaxBytesFromInt()


if __name__ == "__main__":
    Main()
