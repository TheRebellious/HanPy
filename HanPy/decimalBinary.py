import time


# converts a decimal number to binary
def decimalToBinary(input: int):
    output = ""
    while input > 0:
        output += str(input % 2)
        input //= 2
    return output[::-1]


# converts a binary number to decimal
def binaryToDecimal(input: str):
    output = 0
    input = input[::-1]
    for x in range(len(input)):
        if input[x] == "1":
            output += 2 ** (x)
    return output
