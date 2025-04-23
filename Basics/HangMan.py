import random

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

Word_list = ["ticket", "read", "on", "dog", "elephant"]

Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = random.choice(Word_list)
# print(word)

placeholder = ""
for position in range(len(word)) :
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
lives = 0

while not game_over:
    display = ""
    guess = input("Choose a letter? ").lower()
    for letter in word:
        if letter == guess :
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else :
            display += "_"

    print(display)

    

    if guess not in correct_letter:
        lives += 1
        if lives == 6:
            game_over = True
            print("********************You lose********************")
        else :
            print("*************************Wrong guess*************************")
            print(f"***************You have {6 - lives} lives remains***************")

    if "_" not in display:
        game_over = True
        print("********************You won********************") 


    print(Stages[lives])
    print(f"********************You guessed {guess}********************")
    if letter in correct_letter:
        print(f"***************You have already guessed {letter}***************")
