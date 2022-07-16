#----- Hangman (MEDIUM) -----#
import random

bank = ['hello', 'coding', 'codeninjas', 'python', 'umbrella', 'dinosaur', "platform", "lawyer"]
w = list(random.choice(bank))
word = [' '] * len(w)
lives = 5

used = []

while True:
    if lives == 0:
        print("Game Over. You Lose. The word was", w)
        quit()
    elif w == word:
        print(word)
        print("Congrats! You guessed the word.")
        quit()

    print(word)
    guess = input("Guess a letter: ")

    if guess == 'quit':
        quit()
    elif not guess.isalpha(): #not a letter
        print("Invalid Input. Try Again")
    elif guess in w:
        if guess in used:
            print("Letter already used. Try Again.")
        else:
            used.append(guess)
            for i in range(0, len(w)):
                if w[i] == guess:
                    word[i] = guess
    elif guess in used:
        print(guess, "has already been used. Try Again.")
    else:
        print("Wrong guess. Try Again.")
        used.append(guess)
        lives -= 1

    print("Remaining lives:", lives)
    print("Used letters:", used)
    print("-----------------")
    
