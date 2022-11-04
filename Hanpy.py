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