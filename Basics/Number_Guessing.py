import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")
num = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

def make_guess(num):
    global attempts
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess : "))
        if num == guess:
            print("You guessed the correct number. You win")
        else:
            if guess > num:
                print("Too high.")
            else:
                print("Too low.")

            attempts -= 1 
            make_guess(num)
    else:
        print("You have run of of guesses.")

make_guess(num)