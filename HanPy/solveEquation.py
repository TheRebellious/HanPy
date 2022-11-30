import math
import string

detectionString = "()^√*/+-"
answer = ""


# returns a True or False depending on whether the equation is solvable or not
def validate(equation: str):
    LbracketCount = 0
    RbracketCount = 0
    if equation == "":
        return False
    for x in string.ascii_letters:
        if x in equation:
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
        for x in equationList:
            if x[0] in detectionString and x[-1] in detectionString:
                equationList[equationList.index(x)] = "PREV1" + x + "PREV2"
            elif x[0] in detectionString:
                equationList[equationList.index(x)] = "PREV1" + x
            elif x[-1] in detectionString:
                equationList[equationList.index(x)] = x + "PREV1"
    i = 0
    for x in detectionString:
        if x in equation:
            if equation[0] == x and equation[-1] == x:
                equation = "PREV1" + equation + "PREV2"
                equationList.append(equation)
                break
            elif equation[0] == x:
                equation = "PREV1" + equation
                equationList.append(equation)
                break
            elif equation[-1] == x:
                equation = equation + "PREV1"
                equationList.append(equation)
                break

    return equationList


def dissect(equations: list):
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
    return equations


def replacePrev(equations: list):
    replaced = False
    for x in range(len(equations)):
        if replaced:
            break
        if type(equations[x]) == list:
            for y in range(len(equations[x])):
                if type(equations[x][y]) == str:
                    if "PREV" in equations[x][y]:
                        temp = int(equations[x][y][4:])
                        equations[x][y] = equations[x-1]
                        equations.pop(x-1)
                        replaced = True
                        break
    return equations


def solve(equations: list):
    global answer
    for x in equations:
        if ("PREV" in str(x) or type(x) != list) and not (type(x) == list and x[2] == "√" and type(x[0]) == float):
            pass
        elif x[2] == "+":
            temp = str(x[0]) + "+" + str(x[1])
            temp2 = x[0] + x[1]
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
        elif x[2] == "-":
            temp = str(x[0]) + "-" + str(x[1])
            temp2 = x[0] - x[1]
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
        elif x[2] == "*":
            temp = str(x[0]) + "*" + str(x[1])
            temp2 = x[0] * x[1]
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
        elif x[2] == "/":
            temp = str(x[0]) + "/" + str(x[1])
            temp2 = x[0] / x[1]
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
        elif x[2] == "^":
            temp = str(x[0]) + "^" + str(x[1])
            temp2 = x[0] ** x[1]
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
        elif (x[2] == "√") and (type(x[0]) == float):
            temp = "√" + str(x[0])
            temp2 = math.sqrt(x[0])
            answer += temp + " = " + str(temp2) + "\n"
            equations[equations.index(x)] = temp2
    return equations


def getAnswer(equation: str):
    global answer
    if validate(equation):
        equations = analyse(equation)
        dissectedEquations = dissect(equations)
        while "PREV" in str(dissectedEquations):
            dissectedEquations = solve(dissectedEquations)
            dissectedEquations = replacePrev(dissectedEquations)
        solvedEquation = solve(dissectedEquations)
        answer += "\nThe answer is " + str(solvedEquation[0])
        return answer
    else:
        return "The equation is invalid"
