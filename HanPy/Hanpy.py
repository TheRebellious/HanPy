import hexDecimal

# Converts a hexadecimal string into a decimal integer
def hexToDecimal(hexadecimal: str):
    return hexDecimal.hexToDecimal(hexadecimal)

# Converts a decimal integer into a hexadecimal string
def decimalToHex(decimal: int):
    return hexDecimal.decimalToHex(decimal)

# Converts a hexadecimal string into a text string
def hexToText(hexadecimal: str):
    output = ""
    for x in range(0, len(hexadecimal), 2):
        output += chr(hexToDecimal(hexadecimal[x:x+2]))
    return output

# Converts a text string into a hexadecimal string
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