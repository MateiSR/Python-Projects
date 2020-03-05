table = '1  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n2  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n3  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n4  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n5  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n6  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n7  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n8  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n9  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n10 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n11 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n12 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n13 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n14 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n15 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n16 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n17 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n18 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n19 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n20 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n21 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n22 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n23 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n24 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n25 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n26 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n27 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n28 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n29 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n30 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n   A B C D E F G H I K L M N O P Q R S T V X Y Z a b c d e f g'
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30']
planes = 3
height = ''
plane = ''
width = ''
plane_no = ''
three_left = 2
five_left = 1
selected = False
valid = False
five_first = True
three_first = True
temp = False
def cls():
    print("\n" * 100)
print(table)
print('You can place 3 planes, two of them are 3x3, and one is 5x5.')
selected == False
while planes > 0:
    while selected == False:
        if plane == '1' or plane == '2':
            if plane == '1' and three_left > 0:
                selected = True
                three_left -= 1
                pass
            elif plane == '2' and five_left > 0:
                selected = True
                five_left -= 1
                pass
            """
            elif three_left == 0 and five_left == 0:
                print('You have no planes left.')
                break
            if plane == '2' and five_left == 0 and five_first == True:
                print('You have no 5x5 planes left.')
                five_first = False
                break
            if plane == '1' and three_left == 0 and three_first == True:
                print('You have no 3x3 planes left.')
                three_first = False
                break
            """
        else:
            plane = input('Press \'1\' if you want it to be 3x3, or \'2\' for 5x5: ')
    #ask for center 
    while selected == True:
        center = input('Please enter which square you would like the center to be (plane #' + str(planes) + ') [example: B7]: ')
        for i in range(30):
            if len(center) > 3:
                #print('length > 3')
                break
            elif len(center) == 2:
                if center[0] in letters[i]:
                    #print('letter ok! #2')
                    temp = True
                elif center[1] in numbers[i] and temp == True:
                    #print('number ok! #2')
                    valid_center = True
                    #selected = False
            elif len(center) == 3:
                if center[0] in letters[i]:
                    #print('letter ok! #3')
                    temp = True
                elif str(center[1] + center[2]) in numbers[i] and temp == True:
                    #print('number ok! #3')
                    valid_center = True
                    #selected = False
        a = int(letters.index(center[0]))
        if valid_center == True:
            if plane == '1':
                print('3x3')
                table = table.replace('*', '/', 30*(a+1)+int(center[1]))
                print(table)
                table = table.replace('*', 'O', 1)
                print(table)
                table = table.replace('/', '*')
                #cls()
                print(table)
            elif plane == '2':
                print('5x5')
            selected = False
        break