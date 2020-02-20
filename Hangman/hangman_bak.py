import random
import time

name = str(input('Hi! What\'s your name? '))

print('Oh, hi, ' + str(name) + ', let\'s start playing!\nStarting in 1 second..\n')
time.sleep(1)
turns = random.randint(7, 11)
max_turns = turns
print('Start guessing.. NOW! You will have ' + str(turns) + ' turns.')

words = ['red', 'black', 'blue', 'green', 'white', 'yellow']
chosen_word = words[random.randint(0,5)]

found = 0
occurrences = 0

while turns > 0 and found < len(chosen_word):
    success = False
    single_char = True
    guess = input('Guess a character: ')
    if len(guess) > 1:
        print('Please enter a single character.')
        single_char = False
    if single_char == True:
        for char in chosen_word:
            if char == guess.lower():
                occurrences += 1
                print('You guessed the letter \'' + guess +'\' ' + str(occurrences) + ' times.')
                success = True
                found += 1
        if found == len(chosen_word):
            print('You found the word ' + chosen_word + '! Good job!')
        if success == False and turns >= 1:
            turns -= 1
            print(str(turns) + '/' + str(max_turns) +' turns remain' )
        elif success == True and turns >= 1:
            success = False
            occurrences = 0
        if turns == 0:
            print('You didn\'t guess the word. It was: ' + chosen_word +'.')

