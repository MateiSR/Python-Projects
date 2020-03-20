import random # randomization module
from termcolor import cprint # (colored print)

board = [] # board
board_known = [] # Board containing all placed ships
win = False # declare a win boolean
parts = 0 # unused

# Generate board as a list
for x in range(30):
    board.append(["O"] * 30)
# Generate 'cheat sheet' board
for x in range(30):
    board_known.append(["O"] * 30)

# Function: Clear terminal
def cls():
    print("\n" * 100)

# Function: Choose a random row   
def choose_row(board):
    return random.randint(0, len(board) - 3)

# Function: Choose a random column
def choose_col(board):
    return random.randint(0, len(board[0]) - 3)

# Function: Place ships:
def place_ships(n):
    global board_known, parts
    for i in range(1, n):
        chosen_col = choose_col(board_known)
        chosen_row = choose_row(board_known)
        if board_known[chosen_row][chosen_col] != 'X':
            x = random.randint(1, 3)
            if x == 1:
                board_known[chosen_row][chosen_col] = 'X'
                board_known[chosen_row - 1][chosen_col] = 'X'
                board_known[chosen_row + 1][chosen_col] = 'X'
                parts += 3
            elif x == 2:
                board_known[chosen_row][chosen_col] = 'X'
                board_known[chosen_row - 1][chosen_col] = 'X'
                board_known[chosen_row + 1][chosen_col] = 'X'
                board_known[chosen_row + 2][chosen_col] = 'X'
                board_known[chosen_row][chosen_col + 1] = 'X'
                board_known[chosen_row][chosen_col - 1] = 'X'
                parts += 6
            elif x == 3:
                board_known[chosen_row + 1][chosen_col - 1] = 'X'
                board_known[chosen_row + 1][chosen_col - 2] = 'X'
                board_known[chosen_row - 1][chosen_col + 2] = 'X'
                board_known[chosen_row - 1][chosen_col + 1] = 'X'
                parts += 4
        elif board_known[chosen_row][chosen_col] == 'X':
            i -= 1
            pass

# Function: Check if AxY format is valid
def check_coords(guess):
    if guess.find('x') != -1 and len(guess) < 6:
        return True

# Function: Get x and y coordinates from AxY format
def get_coords(guess): # Returns as a tuple
    if guess.find('x') != -1 and len(guess) < 6:
        if len(guess) == 3:
            x = int(guess[0])
            y = int(guess[2])
        elif len(guess) == 4:
            if guess[1] == 'x':
                x = int(guess[0])
                y = int(guess[2] + guess[3])
            elif guess[2] == 'x':
                x = int(guess[0] + guess[1])
                y = int(guess[3])
        elif len(guess) == 5:
            x = int(guess[0] + guess[1])
            y = int(guess[3] + guess[4])
    return x, y
# Returns individual values
def get_x(guess):
    guess = guess.lower().strip()
    if guess.find('x') != -1 and len(guess) < 6:
        if len(guess) == 3:
            x = int(guess[0])
        elif len(guess) == 4:
            if guess[1] == 'x':
                x = int(guess[0])
            elif guess[2] == 'x':
                x = int(guess[0] + guess[1])
        elif len(guess) == 5:
            x = int(guess[0] + guess[1])
    return x

def get_y(guess):
    guess = guess.lower().strip()
    if guess.find('x') != -1 and len(guess) < 6:
        if len(guess) == 3:
            y = int(guess[2])
        elif len(guess) == 4:
            if guess[1] == 'x':
                y = int(guess[2] + guess[3])
            elif guess[2] == 'x':
                y = int(guess[3])
        elif len(guess) == 5:
            y = int(guess[3] + guess[4])
    return y

# Function to convert to string and print board; count rows & columns
def print_board(board_num):
    #board_num = board
    nums = []
    # Count columns
    for i in range(0, len(board)):
        if i < 10:
            board_num[i].insert(0, str(i + 1) + ' ')
        elif i >= 10:
            board_num[i].insert(0, str(i + 1))
            if i == 10: board_num[9][0] = '10' # remove space from previously added '10'
    
    # Count rows
    # Generate a list of numbers 1-30
    for x in range(9):
        nums.append(' ' + str(x + 1))
    for x in range(9, 30):
        nums.append(str(x + 1))
        
    nums = ' '.join(nums) # Convert to string
    print('   ' + nums) # print column count
    # Convert to string
    for row in board_num:
        print('  '.join(row)) # print rows count & board
    print('\n') # Print a blank row
    # Reset board (without nums)
    for i in range(0, len(board)):
        board_num[i].pop(0)

# Function: Check win
def check_win(ships):
    if ships == 0:
        print('\n' + 'Congratulations! You destroyed all the ships!')
        print_board(board_known)
        return True

ships = random.randint(20, 30) # no of ships
turns = random.randint(30, 40) # Number of turns (guesses)
ships_left = ships
print(str(ships) + ' ships have been placed. You will have ' + str(turns) + ' turns (guesses). Good luck!')
place_ships(ships)
# Ask player to guess locations
while turns > 0 and win != True:
    win = check_win(ships_left)
    #print(board)
    print_board(board_known) # Cheat sheet
    print_board(board)
    guess = input('Please guess a location (format: AxB): ')
    
    if guess == 'win': # cheat win
        ships_left = 0
        cls()
        check_win(ships_left)
        break
    
    if guess == 'lose':
        turns = 0
        break
        
    if check_coords(guess) == True:
        x = get_x(guess) - 1
        y = get_y(guess) - 1
    else:
        pass
    cls()
    if board_known[x][y] == 'X':
        board[x][y] == "X"
        print('You hit a ship! Good job! ' + str(ships_left) + ' ships left.')
        ships_left -= 1
    else:
        turns -= 1
        print('Nothing was there. ' + str(turns) + ' turns remaining. ' + str(ships_left) + ' ships left.')
        board[x][y] == "0"
        
if turns == 0:
    cls()
    print('You lost!\n')
    print_board(board_known)