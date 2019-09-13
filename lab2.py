
calendar = [ \
                 range(1, 32), range(1, 29), range(1, 32), \
                 range(1, 31), range(1, 32), range(1, 31), \
                 range(1, 32), range(1, 32), range(1, 31), \
                 range(1, 32), range(1, 32), range(1, 31)  \
            ]

print('Enter date: ')

input       = input()
input       = str(input).split(".")
day         = int(input[0])
month       = int(input[1])

print(day)
print(month)

if  (month == 12 or month == 1  or month == 2)  : print("Winter")
elif(month == 3  or month == 4  or month == 5)  : print("Spring")
elif(month == 6  or month == 7  or month == 8)  : print("Summer")
elif(month == 9  or month == 10 or month == 11) : print("Autumn")
else: print('Error! There\'s only 12 months in year!')

# counters (day and month)
d = 0
m = 1

if((month == 1 or month == 3 or month == 5  or  \
   month  == 7 or month == 8 or month == 10 or  \
   month  == 11) and day > 31):
   print("!Error!\nThere's only 31 days in month: " + str(month))
elif((month == 4 or month == 6 or month == 9 or \
   month == 12) and day > 30):
   print("!Error!\nThere's only 30 days in month: " + str(month))
elif(month == 2 and day > 28):
   print("!Error!\nThere's only 28 days that month: " + str(month))
else:
    for i in calendar:
        for j in i:
            d = d + 1
            if(j == day and m == month): break
        if(m == month): break
        m = m + 1


    print(d, m)
