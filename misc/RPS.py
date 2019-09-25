import random
array = ['Rock', 'Scissors', 'Paper']

print('Hey! Let\'s play rock paper scissors! \nChoose yours: ')
for i,c in enumerate(array):
    print(i, c)
while(True):
    playerChose = input()
    AIChose     = random.choice(array)

    print("AI took " + AIChose)
    if(playerChose == 0 and AIChose == 'Scissors'):
        print("Player took Rock")
        print('Player won!')
        break
    if(playerChose == 1 and AIChose == 'Paper'):
        print("Player took Scissors")
        print('Player won!')
        break
    if(playerChose == 2 and AIChose == 'Rock'):
        print("Player took Paper")
        print('Player won!')
        break
    if(playerChose == 0 and AIChose == 'Paper'):
        print("Player took Rock")
        print('AI wins!')
        break
    if(playerChose == 1 and AIChose == 'Rock'):
        print("Player took Scissors")
        print('AI wins!')
        break
    if(playerChose == 2 and AIChose == 'Scissors'):
        print("Player took Paper")
        print('AI wins!')
        break
    else:
        print('Draw. Repeat!')
