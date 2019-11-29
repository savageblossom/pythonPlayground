f = open("text.txt", "r")

l = f.readline()
# print(l)
line_count = 0
comma_count = 0 # ,
colon_count = 0 # :
semicolon_count = 0 # ;
dot_count = 0 # .


while l:
    # print(l)
    if not l:
        break
    else:
        l = f.readline()
        line_count += 1
        if("," in l):
            comma_count += 1
        elif(":" in l):
            colon_count += 1
        elif(";" in l):
            semicolon_count += 1
        elif("." in l):
            dot_count += 1

print("commas in text: ", comma_count)
print("dots in text: ", dot_count)
print("colons in text: ", colon_count)
print("semicolons in text: ", semicolon_count)
f.close()
