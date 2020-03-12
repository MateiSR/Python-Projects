# + - Plane parts; H - Hit, O - Center
import random

table = '1  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n2  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n3  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n4  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n5  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n6  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n7  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n8  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n9  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n10 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n11 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n12 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n13 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n14 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n15 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n16 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n17 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n18 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n19 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n20 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n21 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n22 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n23 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n24 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n25 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n26 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n27 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n28 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n29 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n30 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n   1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n   |       0       | |         1       | |        2        | 3'

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30']

occupied = []
placed = []
occupied_one = []
occupied_two = []
occupied_three = []
ships = 3
three_left = 2
five_left = 1

def cls():
    print("\n" * 100)

def place_3x3(x, y):
    #print('placing 3x3 ship on ' + str(x) + 'x' + str(y))
    global table, three_left, ships, placed, occupied, occupied_one, occupied_two
    cls()
    placed.append(str(x) + 'x' + str(y))
    print(table)
    if int(x) > 1 and int(y) > 1 and int(x) < 30 and int(y) < 30:
        cls()
        three_left -= 1
        ships -= 1
        # place ship 
        if three_left == 1:
            mid = (x - 1) * 30 + y
            up = (x-2) * 30 + y
            down = x * 30 + y - 2
            right = (x - 1) * 30 + y - 1
            left = (x - 1) * 30 + y - 2
            
            # Middle
            table = table.replace('*', 'A', mid - 1)
            occupied.append(table.find('*'))
            occupied_one.append(table.find('*'))
            table = table.replace('*', 'O', 1)
            table = table.replace('A', '*')
            # Up
            table = table.replace('*', 'B', up - 1)
            occupied.append(table.find('*'))
            occupied_one.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('B', '*')
            # Down
            table = table.replace('*', 'C', down - 1)
            occupied.append(table.find('*'))
            occupied_one.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('C', '*')
            # Right
            table = table.replace('*', 'D', right - 1)
            occupied.append(table.find('*'))
            occupied_one.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('D', '*')
            # Left
            table = table.replace('*', 'E', left - 1)
            occupied.append(table.find('*'))
            occupied_one.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('E', '*')
            
            print('The first 3x3 ship has been placed on square ' + str(x) + 'x' + str(y) + '\n')
            
        elif three_left == 0:
            mid = (x - 1) * 30 + y - 5
            up = (x-2) * 30 + y - 5
            down = x * 30 + y - 7
            right = (x - 1) * 30 + y - 6
            left = (x - 1) * 30 + y - 7
            
            # Middle
            table = table.replace('*', 'A', mid - 1)
            occupied.append(table.find('*'))
            occupied_two.append(table.find('*'))
            table = table.replace('*', 'O', 1)
            table = table.replace('A', '*')
            # Up
            table = table.replace('*', 'B', up - 1)
            occupied.append(table.find('*'))
            occupied_two.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('B', '*')
            # Down
            table = table.replace('*', 'C', down - 1)
            occupied.append(table.find('*'))
            occupied_two.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('C', '*')
            # Right
            table = table.replace('*', 'D', right - 1)
            occupied.append(table.find('*'))
            occupied_two.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('D', '*')
            # Left
            table = table.replace('*', 'E', left - 1)
            occupied.append(table.find('*'))
            occupied_two.append(table.find('*'))
            table = table.replace('*', '+', 1)
            table = table.replace('E', '*')
            
            print('The first 3x3 ship has been placed on square ' + str(x) + 'x' + str(y) + '\n')
        
        print(table)


    else:
        print('X and Y coordinates should be greater than 1 and less than 30.')

def place_5x5(x, y):
    #print('placing 5x5 ship on ' + str(x) + 'x' + str(y))
    global table, five_left, ships, placed, occupied, occupied_three
    cls()
    print(table)
    if int(x) > 2 and int(y) > 2 and int(x) < 29 and int(y) < 29:
        print('A 5x5 ship has been placed on square ' + str(x) + 'x' + str(y) + '\n')
        five_left -= 1
        ships -= 1
        middle = (x - 1) * 30 + y - 1 - 9
        up = (x-2) * 30 + y - 1 - 9
        up_two = (x-3) * 30 + y - 1 - 9
        down = x * 30 + y - 4 - 9
        down_two = (x + 1) * 30 + y - 5 - 9
        right = (x - 1) * 30 + y - 3 - 9
        left = (x - 1) * 30 + y - 5 - 9
        # place ship
        # Middle
        table = table.replace('*', 'A', middle - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', 'O', 1)
        table = table.replace('A', '*')
        # Up
        table = table.replace('*', 'B', up - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('B', '*')
        # Up 2
        table = table.replace('*', 'F', up_two - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('F', '*')
        # Down
        table = table.replace('*', 'C', down - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('C', '*')
        # Down 2
        table = table.replace('*', 'G', down_two - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('G', '*')
        # Right
        table = table.replace('*', 'D', right - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('D', '*')
        # Right 2
        table = table.replace('*', 'H', right - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('H', '*')
        # Left
        table = table.replace('*', 'E', left - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('E', '*')
        # Left 2
        table = table.replace('*', 'I', left - 1)
        occupied.append(table.find('*'))
        occupied_three.append(table.find('*'))
        table = table.replace('*', '+', 1)
        table = table.replace('I', '*')
        
        print(table)
    else:
        print('X and Y coordinates should be greater than 2 and less than 29.')


print(table)
print('You can place 3 ships, two of them are 3x3, and one is 5x5.')

while ships > 0:
    
    while three_left > 0:
        if three_left == 2:
            print('1st 3x3 ship!')
            location = input('Where do you want to place the ship? (format: XxY): ').lower().strip()
            
            while True:
                if location.find('x') != -1 and len(location) < 6:
                    if len(location) == 3:
                        x = int(location[0])
                        y = int(location[2])
                    elif len(location) == 4:
                        if location[1] == 'x':
                            x = int(location[0])
                            y = int(location[2] + location[3])
                        elif location[2] == 'x':
                            x = int(location[0] + location[1])
                            y = int(location[3])
                    elif len(location) == 5:
                        x = int(location[0] + location[1])
                        y = int(location[3] + location[4])
                    break
            place_3x3(x, y)
            
        if three_left == 1:
            print('2nd 3x3 ship!')
            
            location = input('Where do you want to place the ship? (format: XxY): ').lower().strip()
            
            while True:
                if location.find('x') != -1 and len(location) < 6:
                    if len(location) == 3:
                        x = int(location[0])
                        y = int(location[2])
                    elif len(location) == 4:
                        if location[1] == 'x':
                            x = int(location[0])
                            y = int(location[2] + location[3])
                        elif location[2] == 'x':
                            x = int(location[0] + location[1])
                            y = int(location[3])
                    elif len(location) == 5:
                        x = int(location[0] + location[1])
                        y = int(location[3] + location[4])
                    break
            place_3x3(x, y)
            
    if three_left == 0:
        print('You have finished placing your 3x3 ships. Place your 5x5 ship.')
    
    while five_left > 0:
            location = input('Where do you want to place the ship? (format: XxY): ').lower().strip()
            while True:
                if location.find('x') != -1 and len(location) < 6:
                    if len(location) == 3:
                        x = int(location[0])
                        y = int(location[2])
                    elif len(location) == 4:
                        if location[1] == 'x':
                            x = int(location[0])
                            y = int(location[2] + location[3])
                        elif location[2] == 'x':
                            x = int(location[0] + location[1])
                            y = int(location[3])
                    elif len(location) == 5:
                        x = int(location[0] + location[1])
                        y = int(location[3] + location[4])
                    break
            place_5x5(x, y)
    
turns = random.randint(8, 12)
hit = False

if ships == 0:
    print('You\'re done placing ships! Get ready to battle!')
    print('You are going to have ' + str(turns) + ' turns to destroy all the ships. If you don\'t, you lose. Good luck!')

while turns > 0:
    #cls()
    print(table)
    print('You have ' + str(turns) + ' turns left.')
    guess = input('Guess a square (AxB): ').lower().strip()
    
    if guess.find('x') != -1 and len(guess) < 6:
        if len(guess) == 3:
            x = int(guess[0])
            y = int(guess[2])
        elif len(guess) == 4:
            if location[1] == 'x':
                x = int(guess[0])
                y = int(guess[2] + guess[3])
            elif location[2] == 'x':
                x = int(guess[0] + guess[1])
                y = int(guess[3])
        elif len(guess) == 5:
            x = int(guess[0] + guess[1])
            y = int(guess[3] + guess[4])
        
        if x < 10:
            id = (x - 1) * 62 + 2 * y + 3
        elif x >= 10:
            id = (x - 1) * 62 + 2 * y + 4
        
        print('\n' + str(x) + ';' + str(y))
        print(occupied)
        print('id: ' + str(id))
        
        
        for i in range(len(occupied)):
            if occupied[i] == id:
                hit = True
                hit_id = id
        
        if hit != True:
            turns -= 1
        if hit == True:
            print('You hit a ship!')
            hit = False
            #replace with H
            occupied.remove(id)
            table = table[:hit_id] + 'H' + table[hit_id+1:]
        print(table[id])
    # if destroyed all ships, pass and print