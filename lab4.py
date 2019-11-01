# Lab 4

# Checking to see if x is a number
def isNumber(item):
    try:
        float(item)
        return True
    except ValueError:
        return False

def readExpression():
    # Gets string and deletes whitespace
    astring = raw_input('Enter your expression: \n')
    astring = astring.replace(" ", "")

    # After that it will check if there are any unsupported characters in the string
    for item in astring:
        if item not in '0123456789+-*/.()':
            print ("Error! \nUnsupported character: " + item)
            exit()

    # Then it creates the list and adds each individual character to the list
    list = []
    for item in astring:
        list.append(item)

    # It combines individual numbers into actual numbers based on input
    count = 0
    while count < len(list) - 1:
        if isNumber(list[count]) and isNumber(list[count + 1]):
            list[count] += list[count + 1]
            # print(list[count])
            # print(list[count+1])
            del list[count + 1]
        elif isNumber(list[count]) and list[count + 1] == ".":
            list[count] += list[count + 1] + list[count + 2]
            del list[count + 2]
            del list[count + 1]
        else:
            count += 1

    # print(list)
    return list


def performOperation(n1, operand, n2):
    if operand == "+":
        return str(float(n1) + float(n2))
    elif operand == "-":
        return str(float(n1) - float(n2))
    elif operand == "*":
        return str(float(n1) * float(n2))
    elif operand == "/":
        try:
            n = str(float(n1) / float(n2))
            return n
        except ZeroDivisionError:
            print ("Error! Division by zero!")
            exit()


main = readExpression()

# If the length of the list is 1, there is only 1 number, meaning an answer has been reached.
while len(main) != 1:
    # print("".join(main))
    '''
    If there are parentheses around a single list item, the list item is
    obviously just a number, eliminate parentheses.
    Will check to see if the first parentheses exists first so that it does not
    throw an index error
    '''
    for i, e in enumerate(main):
        if main[i] == "(":
            if main[i + 2] == ")":
                del main[i + 2]
                del main[i]

    # Multiply OR Divide
    for i, e in enumerate(main):
        if main[i] in ["*", "/"] and not (main[i+1] in '()' or main[i-1] in '()'):
            main[i - 1] = performOperation(main[i - 1], main[i], main[i + 1])
            del main[i + 1]
            del main[i]

    # Add OR Substract
    for i, e in enumerate(main):
        if main[i] in ["+", "-"] and not (main[i+1] in '()' or main[i-1] in '()'):
            main[i - 1] = performOperation(main[i - 1], main[i], main[i + 1])
            del main[i + 1]
            del main[i]


print(main[0])
