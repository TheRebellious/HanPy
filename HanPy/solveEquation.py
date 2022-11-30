detectionString = "()^√*/+-"

# returns a True or False depending on whether the equation is solvable or not


def validate(equation: str):
    LbracketCount = 0
    RbracketCount = 0
    if equation == "":
        return False
    for x in equation:
        if x == '(':
            LbracketCount += 1
        elif x == ')':
            RbracketCount += 1
    if LbracketCount != RbracketCount:
        return False
    elif equation[0] == ')':
        return False
    elif equation[-1] == '(':
        return False
    elif equation[0] == '*' or equation[0] == '/' or equation[0] == '^' or equation[0] == '+' or equation[0] == '-':
        return False
    elif equation[-1] == '*' or equation[-1] == '/' or equation[-1] == '^' or equation[-1] == '+' or equation[-1] == '-':
        return False
    else:
        return True

# returns a list of the to be solved equations to get to the final answer


def getBrackets(equation: str):
    brackets = []
    # find where all the brackets are
    for x in range(len(equation)):
        if equation[x] == '(':
            brackets.append([x, "("])
        elif equation[x] == ')':
            brackets.append([x, ")"])
    # find all bracket pairs
    bracketPairs = []
    while brackets != []:
        i = 0
        for x in brackets:
            if x[1] == "(":
                i += 1
            elif x[1] == ")":
                i -= 1
            if i == 0:
                bracketPairs.insert(0, [brackets[0][0], x[0]])
                brackets.pop(0)
                brackets.remove(x)
                break
    return bracketPairs


def analyse(equation: str):
    global detectionString
    print(equation)
    equationList = []
    # look if there is a bracket in the equation
    if detectionString[0] in equation:

        # get all of the equations in the brackets
        bracketPairs = getBrackets(equation)
        while bracketPairs != [] and equation != "":
            for x in bracketPairs:
                equationList.append(equation[x[0] + 1:x[1]])
                equation = equation[:x[0]] + "" + equation[x[1]+1:]
                bracketPairs.remove(x)
                bracketPairs = getBrackets(equation)
                break
        print(equationList)
        for x in equationList:
            if x[0] in detectionString and x[-1] in detectionString:
                equationList[equationList.index(x)] = "PREV1" + x + "PREV2"
            elif x[0] in detectionString:
                equationList[equationList.index(x)] = "PREV1" + x
            elif x[-1] in detectionString:
                equationList[equationList.index(x)] = x + "PREV1"
    return equationList


def solve(equations: list):
    global detectionString
    # get the numbers and operators from x in equations
    for x in range(len(equations)):
        numberList = []
        for y in detectionString:
            numberList = equations[x].split(y)
            if len(numberList) > 1:
                break
        for i in range(len(numberList)):
            if numberList[i] != "PREV1" and numberList[i] != "PREV2":
                numberList[i] = float(numberList[i])
        equations[x] = [numberList[0], numberList[1], y]
    print(str(equations)[1:-1])


# equation = "(2*15)+(304-2)"
equation = "((2+2)*(15+4))*(3+3)"
if validate(equation):
    equations = analyse(equation)
    solve(equations)
