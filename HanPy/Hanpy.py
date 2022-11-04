import hexDecimal

def hexToDecimal(hexadecimal: str):
    return hexDecimal.hexToDecimal(hexadecimal)

def decimalToHex(decimal: int):
    return hexDecimal.decimalToHex(decimal)

def hexToText(hexadecimal: str):
    output = ""
    for x in range(0, len(hexadecimal), 2):
        output += chr(hexToDecimal(hexadecimal[x:x+2]))
    return output

def textToHex(text: str):
    output = ""
    for x in text:
        output += decimalToHex(ord(x))
    return output

# returns a random 2 dimensional list of hexadecimals and their decimal values
def randomHexList():
    from random import randint
    output = []
    for x in range(randint(1, 10)):
        randomint = decimalToHex(randint(0, 255))
        output.append([hexToDecimal(randomint), randomint])
    return output