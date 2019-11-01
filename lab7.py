def mult(a, b):
    if(b <= 0):
        return 0
    else:
        return mult(a, b-1) + a

print(mult(4, 4))
