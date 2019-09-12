
calendar = [ \
                 range(1, 32), range(1, 29), range(1, 32),\
                 range(1, 31), range(1, 32), range(1, 31),\
                 range(1, 32), range(1, 32), range(1, 31),\
                 range(1, 32), range(1, 32), range(1, 31) \
            ]

print('Enter date: ')

input       = input().split(".")
day         = int(input[0])
month       = int(input[1])

print(day)
print(month)

if  (month == 12 or month == 1 or month == 2) : print("Winter")
elif(month == 3 or month == 4 or month == 5)  : print("Spring")
elif(month == 6 or month == 7 or month == 8)  : print("Summer")
elif(month == 9 or month == 10 or month == 11): print("Autumn")
else: print('Error! There\'s only 12 months in year!')

d = 0
m = 1

for i in calendar:
    for j in i:
        d = d + 1
        if(j == day and m == month): break
    m = m + 1
    if(m == month): break



print(d, m)
