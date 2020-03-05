import random

def cls():
    print("\n" * 100)

words = ['red', 'black', 'blue', 'violet', 'white', 'orange', 'yellow']
x = random.randint(0, 6)
chosen_word = words[x]
blanks = []

global drawings

drawings = ['''
  -----
  |   |
      |
      |
      |
      |
*********''', '''
  -----
  |   |
  O   |
      |
      |
      |
*********''', '''
  -----
  |   |
  O   |
  |   |
  |   |
      |
      |
*********''', '''
  -----
  |   |
  O   |
 /|   |
  |   |
      |
      |
*********''', '''
  -----
  |   |
  O   |
 /|\  |
  |   |
      |
      |
*********''', '''
  -----
  |   |
  O   |
 /|\  |
  |   |
 /    |
      |
*********''', '''
  -----
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
*********''']

for i in range(len(chosen_word)):
    blanks.append('_')

turns = 6
wrong = 0
while turns > 0:
    cls()
    print('DEBUG: Chosen word: ' + chosen_word)
    print(str(turns) + ' turns left')
    print(drawings[wrong])
    print(' '.join(blanks))

    correct = False
    guess = input('Guess a character: ')
    while len(guess) != 1:
        guess = input('Guess a character: ')

    for j in range(len(chosen_word)):
        if chosen_word[j] == guess:
            blanks[j] = guess
            correct = True
        else:
            pass

    if correct == False:
        turns -= 1 
        wrong += 1
        if turns > 0:
            pass
        elif turns == 0:
            print(drawings[6])
            print('You didn\'t guess the word: ' + chosen_word)
    
    blanks_string = ''.join(blanks)

    if blanks_string == chosen_word:
        print('You found the word: ' + chosen_word)
        break
    
    


        


