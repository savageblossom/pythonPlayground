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

def innermostParenthesis(text):
    if not '(' and not ')' in text:
        return text
    open  = text.index('(')
    close = text.rindex(')')

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
