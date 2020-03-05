# + unde este plane, # cand e lovit
table = '1  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n2  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n3  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n4  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n5  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n6  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n7  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n8  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n9  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n10 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n11 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n12 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n13 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n14 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n15 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n16 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n17 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n18 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n19 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n20 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n21 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n22 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n23 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n24 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n25 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n26 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n27 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n28 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n29 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n30 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n   1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n   |       0       | |         1       | |        2        | 3'

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30']

ships = 3
three_left = 2
five_left = 1

def cls():
    print("\n" * 100)

def place_3x3(x, y):
    print('placing 3x3 ship on ' + str(x) + 'x' + str(y))

def place_5x5(x, y):
    print('placing a 5x5 ship')
    print('placing 3x3 ship on ' + str(x) + 'x' + str(y))


print(table)
print('You can place 3 planes, two of them are 3x3, and one is 5x5.')

while ships > 0:
    type = input('Input 1 for 3x3, and 2 for 5x5: ') 
    if type == '1':
        if three_left > 0:
            three_left -= 1
            ships -= 1
            location = input('Where do you want to place the ship? (format: XxY): ')
            while True:
                if location.find('x') != -1 and len(location) < 6:
                    x = int(location[0])
                    y = int(location[2])
                    place_3x3(x, y)
                    break
                else:
                    location = input('Where do you want to place the ship? (format: XxY): ')
        elif three_left == 0:
            print('You have no 3x3 ships left to place.')
    
    elif type == '2':
        if five_left == 1:
            five_left -= 1
            ships -= 1
            location = input('Where do you want to place the ship? (format: XxY): ')
            while True:
                if location.find('x') != -1 and len(location) < 6:
                    x = int(location[0])
                    y = int(location[2])
                    place_5x5(x, y)
                    break
                else:
                    location = input('Where do you want to place the ship? (format: XxY): ')
        elif five_left == 0:
            print('You have no 5x5 ships left to place.')

if ships == 0:
    print('You\'re done placing ships! Get ready to battle!')

while True:
    pass
    # if destroyed all ships, pass and print