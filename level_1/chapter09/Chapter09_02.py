# 행맨

import time
import random
import csv
import winsound

print("Start Loading...")
print()
time.sleep(0.5)

words = []

with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)
word = q[0].strip()

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
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print("Congratulations! The Guesses is correct.")
        break

    print()
    print()
    print('Hint : {}'.format(q[1].strip()))

    guess = input('Guess a character: ')

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Oops! Wrong")
        print("You have", turns, 'more guesses!')

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print("Game Over!")