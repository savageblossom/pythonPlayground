arr = [5, 4, 3, 2, 1]
# print(arr)
# del(arr[2])
# print(arr)

for i, e in enumerate(arr):
    arr[i] *= 2
i = len(arr)
while(True):
    x = raw_input('Enter something #' + str(i) + ": \n")
    if(x) == "0":
        break
    else:
        arr.append(x)
    i += 1
print(arr)
