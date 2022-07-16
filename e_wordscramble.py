#----- WORD SCRAMBLE (EASY) -----#
import random

bank = ['hello', 'coding', 'codeninjas', 'python', 'umbrella', 'dinosaur', "platform", "lawyer"]
w = random.choice(bank)
word = list(w)
random.shuffle(word)

lives = 5

while True:
    print(word)
    print("Remaining Guesses:", lives)
    guess = input("Guess the word: ")

    if guess == w:
        print("Congrats! You guess the word correctly.")
        quit()
    elif guess == 'quit':
        quit()
    else:
        lives -= 1
        if lives == 0:
            print("You are out of lives.")
            print("The word was:", w)
            quit()
        print("Wrong guess. Try again.")