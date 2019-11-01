import re

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
# print('Enter your expression (i.e. 13+37/14+88): ')
#
# # 2 + 2 * 6
# initialList  = raw_input()
# listOfOperations = re.findall(r"\W+", initialList)
# numberList = re.findall(r'\d+', initialList)
# expressionList  = []
# length = len(listOfOperations) + len(numberList)
#
# for x in numberList:
#     expressionList.append(x)
# print(numberList)
# print(listOfOperations)

def solve(str):
    # Removal of spaces
    listToWorkWith = ""
    for x in str:
        if x != " ":
            listToWorkWith += x

    listOfNumbers    = re.findall(r'\d+', listToWorkWith)
    listOfOperations = re.findall(r'\W+', listToWorkWith)
    expressionList   = []
    length           = len(listOfNumbers) + len(listOfOperations)

    for x in range(1, len(listOfNumbers)+1):
        expressionList.append(listOfNumbers[x])
        if(listOfOperations.index(x)):
            expressionList.append(listOfOperations[x])
    return expressionList

print(solve('123+123/123'))

# for x in listOfOperations:
#     if(x == '*') :
#         initialList[]

# getCharacter = ""
# if('+' in list(initialList))  : getCharacter = '+'
# elif('-' in list(initialList)): getCharacter = '-'
# elif('*' in list(initialList)): getCharacter = '*'
# elif('/' in list(initialList)): getCharacter = '/'
# else : print('Error! Enter valid characters!')
# # print(getCharacter)
#
# if(getCharacter in list(initialList)) :
#     a = int((initialList.split(getCharacter))[0])
#     b = int((initialList.split(getCharacter))[1])
#     if(getCharacter == '+')   : result = a + b
#     elif(getCharacter == '-') : result = a - b
#     elif(getCharacter == '*') : result = a * b
#     elif(getCharacter == '/') :
#         if(a == 0) : print('Error! Division by zero!')
#         else : result = a / b
#     else : print('Error! Enter valid characters!')
#     print(result)
