array = range(0, 100, 5)

for i, c in enumerate(array):
    print(i, c)

# Creating function
def isTrue(element):
    if(element == True):
        return True
    else:
        return False

# Calling a function
print(isTrue(True))

# Working with files
x = file("misc/file.txt", "r")
for line in x:
    print(line)
x.close()
