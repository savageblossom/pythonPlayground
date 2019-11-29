def mult(a, b):
    if(b <= 0):
        return 0
    else:
        print('b equals',b-1)
        return mult(a, b-1) + a

print('Enter number a: ')
a = input();
print('Enter number b: ')
b = input();

print(mult(a, b))
