hexdict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}

decdict = {v: k for k, v in hexdict.items()}


def hexToDecimal(input: str):
    input = input[::-1]
    values = []
    for x in input:
        values.append(hexdict[x]*(16**len(values)))
    output = 0
    for x in values:
        output += x
    return output


def decimalToHex(input: int):
    og = input
    totalLen = len(str(input))
    while input > 15:
        input /= 16
    values = []
    values.append(int(input))
    remainder = input - values[0]
    for x in range(1, totalLen):
        input = remainder * 16
        values.append(int(input))
        remainder = input - int(input)
    
    if values[len(values)-1] == 0 and og < 128:
        values.remove(0)
    if values[0] == 0 and og < 256:
        values.remove(0)
    output = ""
    for x in values:
        output += decdict[x]
    return output


print(decimalToHex(86))
