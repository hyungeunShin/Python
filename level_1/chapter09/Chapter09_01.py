# 행맨

import time

print("Start Loading...")
print()
time.sleep(0.5)

word = "secret"
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
        
    if failed == 0:
        print()
        print()
        print("Congratulations! The Guesses is correct.")
        break

    print()
    print()
    
    guess = input('Guess a character: ')

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Oops! Wrong")
        print("You have", turns, 'more guesses!')

        if turns == 0:
            print("Game Over!")