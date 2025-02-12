import sys
from math import ceil, floor


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


# masque pour representer la partie Byte(8 premières bits)
# d'un entier int (number1)
def calculateByteEquivalent(number1, number2):
    byte_number1 = number1 & 0xFF;
    byte_number2 = number2 & 0xFF;
    return [byte_number1, byte_number2]

def getTemperatureMille(temperature):
    mille = floor(temperature / 1000)
    cent = floor((temperature - mille * 1000) / 100)
    diz = floor((temperature - mille * 1000 - cent * 100) / 10)
    units = temperature % 10

    print("units vaut=" + str(mille) + " " + str(cent) + " " + str(diz) + " " + str(units))

def getTemperatureDecimal(temperature):
    mille = 0
    cent = 0
    diz = floor((temperature - mille * 1000 - cent * 100) / 10)
    units = temperature % 10

    print("units vaut="  + str(diz) + " " + str(units))
    print("units bytes vaut=" +  str(getBytesFromInt(diz)) + " " + str(getBytesFromInt(units)))


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
    # DECIMAL
    temperature = 7290
    mille = floor(temperature / 1000)
    cent = floor((temperature - mille * 1000) / 100)
    diz = floor((temperature - mille * 1000 - cent * 100) / 10)
    units = temperature % 10

    getTemperatureMille(1245)
    getTemperatureDecimal(2565)

if __name__ == "__main__":
    Main()
