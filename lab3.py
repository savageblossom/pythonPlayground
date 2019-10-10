#
# # Task 1
# print('Enter number a: ')
# a = int(raw_input())
# print('Enter number b: ')
# b = int(raw_input())
# print('Enter operation (+, -, *, /): ')
# op = str(raw_input())
#
# if(op == "+") : print(a + b)
# elif(op == "-") : print(a - b)
# elif(op == "*") : print(a * b)
# elif(op == "/") :
#     if(a != 0) : print(a / b)
#     else: print('Error. Division by zero!')


# Task 2

'''
    Whenever isNumber(x) exists, it is checking to see if x is a number, obviously.
'''
def isNumber(item):
    try:
        float(item)
        return True
    except ValueError:
        return False


def readExpression():
    # First part gets string and deletes whitespace
    astring = "2 + 3 * (24 - 666 / 333) - 69 + (1488 - (666 * (1+1)))"
    astring = astring.replace(" ", "")

    # Next it will check if there are any unsupported characters in the string
    for item in astring:
        if item not in '0123456789+-*/.()':
            print ("Unsupported Character: " + item)
            exit()

    # Then it creates the list and adds each individual character to the list
    list = []
    for item in astring:
        list.append(item)

    count = 0

    # It combines individual numbers into actual numbers based on user input
    while count < len(list) - 1:
        if isNumber(list[count]) and list[count + 1] == "(":
            print ("Program does not accept parentheses directly after\
             number, must have operator in between.")
            exit()
        if isNumber(list[count]) and isNumber(list[count + 1]):
            list[count] += list[count + 1]
            # print(list[count])
            # print(list[count+1])
            del list[count + 1]
        elif isNumber(list[count]) and list[count + 1] == ".":
            try:
                x = list[count+2]
            except IndexError:
                print ("Your formatting is off somehow.")
                exit()
            if isNumber(list[count + 2]):
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
            print ("You tried to divide by 0.")
            exit()


main = readExpression()
emergency_count = 0

# Makes code shorter, short for parentheses
P = '()'

# If the length of the list is 1, there is only 1 number, meaning an answer has been reached.
while len(main) != 1:
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

    # After that is done, it will multiply and divide what it can
    for i, e in enumerate(main):
        if main[i] in ["*", "/"] and not (main[i+1] in P or main[i-1] in P):
            main[i - 1] = performOperation(main[i - 1], main[i], main[i + 1])
            del main[i + 1]
            del main[i]

    # Then it will add and substract what it can
    for i, e in enumerate(main):
        if main[i] in ["+", "-"] and not (main[i+1] in P or main[i-1] in P):
            main[i - 1] = performOperation(main[i - 1], main[i], main[i + 1])
            del main[i + 1]
            del main[i]


print(main[0])
