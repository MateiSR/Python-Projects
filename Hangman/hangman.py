import random
import time

name = str(input('Hi! What\'s your name? '))

print('Oh, hi, ' + str(name) + ', let\'s start playing!\nStarting in 1 second..\n')
time.sleep(1)
turns = 6
max_turns = turns
print('Start guessing.. NOW! You will have ' + str(turns) + ' turns.')

words = ['red', 'black', 'blue', 'violet', 'white', 'orange']
chosen_word = words[random.randint(0,5)]
initial_chosen_word = chosen_word


found = 0
occurrences = 0

word_length = len(initial_chosen_word)
field = '_' * word_length
field_list = list(field)
print('DEBUG - Chosen word: ' + initial_chosen_word) # for debug

global progress_field
progress_field = field

global drawings

drawings = ['''
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
 
def cls():
    print("\n" * 100)

while turns > 0 and progress_field != initial_chosen_word:
    #and found < len(chosen_word)
    success = False
    single_char = True
    found_chars = ''
    multiple_occurences = False
    guess = input('Guess a character: ')

    if len(guess) > 1:
        print('Please enter a single character.')
        single_char = False
    
    if single_char == True:
        for char in chosen_word:
            if char == guess.lower():

                if chosen_word.count(char) > 1:
                    multiple_occurences = True
                cls()
                print('You guessed the letter \'' + guess +'\' ' + str(chosen_word.count(char)) + ' times.')
            
                position = initial_chosen_word.find(guess)
                field_list[position] = char
                progress_field = ''.join(field_list)

                success = True
                found += 1
                found_chars = found_chars + char
                chosen_word = chosen_word.replace(char, '')
        
        if progress_field == initial_chosen_word:
            print('You found the word ' + initial_chosen_word + '! Good job!')
        
        if success == False and turns >= 1:
            cls()
            turns -= 1
            print(str(turns) + '/' + str(max_turns) +' turns remain' )
            print('Completion: ' + progress_field)

        elif success == True and turns >= 1:
            success = False
            print('Completion: ' + progress_field)
        
        if turns == 0:
            print('You didn\'t guess the word. It was: ' + initial_chosen_word +'.')
        
        if turns == 6:
            print(drawings[0])
        elif turns == 5:
            print(drawings[1])
        elif turns == 4:
            print(drawings[2])
        elif turns == 3:
            print(drawings[3])
        elif turns == 2:
            print(drawings[4])
        elif turns == 1:
            print(drawings[5])
        elif turns == 0:
            print(drawings[6] + '\n' * 2)

