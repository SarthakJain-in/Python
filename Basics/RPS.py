import random

rock = '''                   
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
      '''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissor = '''
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \

|___/\___|_|___/___/\___/|_|  |___/
'''

rps = [rock, paper, scissor]

random_index = random.randint(0, 2)

user_input = int(input("Choose your side from 0 for rock, 1 for paper and 2 for scissor : "))

print("You")
print(rps[user_input])

print("\n\nComputer")
print(rps[random_index] + "\n")

if user_input == 0 :
    if random_index == 1 :
        print("You lose")
    elif random_index == 2 :
        print("You won")
    else :
        print("Draw")

if user_input == 1 :
    if random_index == 2 :
        print("You lose")
    elif random_index == 0 :
        print("You won")
    else :
        print("Draw")

if user_input == 2 :
    if random_index == 0 :
        print("You lose")
    elif random_index == 1 :
        print("You won")
    else :
        print("Draw")
