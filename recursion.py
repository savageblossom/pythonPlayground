#factorial test
def factorial(n):
    if(n >= 1):
        return n*factorial(n-1)
    else: return 1
print(factorial(-5))

# (a (b (c (d))))
string = '(a (b (c)))'
def deepmostParentheses(str):
    if not '(' or not ')' in str:
        return str
    else:
        open  = str.index('(')
        close = str.rindex(')')
        str = str[open+1:close]
        # print(str)
        return deepmostParentheses(str)

def solve(str):
    return eval(removeSpaces(deepmostParentheses(str)))


def removeSpaces(str):
    listToWorkWith = ""
    for x in str:
        if(x != ' '):
            listToWorkWith += x
    return listToWorkWith

print(solve('((1 + (11 + 10) + 33) * 2 / 2)'))
