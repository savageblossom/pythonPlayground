print('Greetings!\nThere\'s no list detected. Wanna create new empty list? (y/n)')
answer = raw_input()
if(answer == "y"):
    myList = []
    print('New list has beed created. How it looks:')
    print(myList)
    print('Want to modify it? (y/n)')
    answer = raw_input()
    if(answer == "y"):
        print('Type /help to get all commands to work with your list')
        while(True):

            action = raw_input().split(' ')

            if  ('/help' in action):
                helpList = [
                             '/help - prints all commands and how to use them', \
                             '/append <element> - appends an element to the end of the list', \
                             '/insert <index> <element> - inserts an element into index', \
                             '/remove <index> - removes element at certain index', \
                             '/sort <asc:desc> - sorts the list by ascedning or by descending', \
                             '/show - shows all elements of the list', \
                             '/len - return length of the list', \
                             '/exit - exits program'
                           ]
                for e in helpList:
                    print(e)

            elif('/append' in action):
                myList.append(action[1])
                print('An element "' + action[1] + '" has been succesfully added to the list!')
                print(myList)

            elif('/insert' in action):
                myList.insert(int(action[1]), action[2])
                print('An element "' + action[2] + '" has been succesfully inserted into the list at index: ' + action[1])
                print(myList)

            elif('/remove' in action):
                del myList[int(action[1])]
                print('An element "' + action[1] + '" has been succesfully deleted at index ' + action[1])
                print(myList)

            elif('/sort' in action):
                if(action[1] == 'asc'):
                    myList.sort()
                    print('List has been succesfully sorted by ascendending!')
                    print(myList)
                if(action[1] == 'desc'):
                    myList.sort(reverse=True)
                    print('List has been succesfully sorted by descending!')
                    print(myList)

            elif('/show' in action):
                print(myList)

            elif('/len' in action):
                print('Count of elements in list: ')
                print(len(myList))

            elif('/exit' in action):
                print('Bye!')
                break
else:
    print('Bye!')
