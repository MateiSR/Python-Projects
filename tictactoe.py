from graphics import *
from sys import exit

# Generate player input list
inputs = []
for i in range(3):
    inputs.append([None, None, None])

def generate_window(): # generate window & draw grid lines
    global window
    window = GraphWin('Tic Tac Toe - graphics.py', 300, 300) # Generate window

    # Draw board
    for i in range(3):
        # Draw horizontal lines inside window
        horizontal_lines = Line(Point(0, 100 * i), Point(300, 100 * i))
        horizontal_lines.draw(window)
    for i in range(3):
        # Draw vertical lines inside window
        vertical_lines = Line(Point(100 * i, 0), Point(100 * i, 300))
        vertical_lines.draw(window)

def start_game(): # Start game 
    global inputs, window
    for i in range(9):
        print(i)
        # Player X
        if i % 2 == 0:
            print('>>> Player X: Select a square')
            Xmouse = window.getMouse() # get mouse location
            Xx = Xmouse.getX()
            Xy = Xmouse.getY()
            print('X'+str(Xx) + ' Y' + str(Xy))
            playerX(inputs, window, Xx, Xy)
            if check_win(inputs) == True:
                print('Player X won')
                break
        
        # Player O
        if i % 2 != 0:
            print('>>> Player O: Select a square')
            Omouse = window.getMouse() # get mouse location
            Ox = Omouse.getX()
            Oy = Omouse.getY()
            print('X'+str(Ox) + ' Y' + str(Oy))
            playerO(inputs, window, Ox, Oy)
            if check_win(inputs) == True: #check for win
                print('Player O won')
                break

def show_window(): # Show window
    global inputs, window
    generate_window() # Generate window
    start_game()
    #window.close()
    exit()

def get_square(x, y): # x and y are mouse positions
    # y: 0-100 > row 1; 100-200 > row 2; 200-300: row 3
    # Row 1
    if y > 0 and y <= 100:
        if x > 0 and x < 100:
            return 0
        if x > 100 and x <= 200:
            return 1
        if x > 200 and x <= 300:
            return 2
    # Row 2
    if y > 100 and y <= 200:
        if x > 0 and x < 100:
            return 3
        if x > 100 and x <= 200:
            return 4
        if x > 200 and x <= 300:
            return 5
    # Row 3
    if y > 200 and y <= 300:
        if x > 0 and x < 100:
            return 6
        if x > 100 and x <= 200:
            return 7
        if x > 200 and x <= 300:
            return 8

def draw_circle(center): # Draw O
    circle = Circle(center, 40)
    circle.setWidth(5)
    circle.setOutline('red')
    circle.draw(window)
    
def draw_x(diag1, diag2): # Draw X
    diag1.setWidth(5)
    diag2.setWidth(5)
    diag1.draw(window)
    diag2.draw(window)

def playerO(inputs, window, Ox, Oy): # Player O Place
    square = get_square(Ox, Oy)
    print('square: ' + str(square))
    if square == 0:
        center = Point(50, 50)
        inputs[0][0] = 'O'
    elif square == 1:
        center = Point(150, 50)
        inputs[1][0] = 'O'
    elif square == 2:
        center = Point(250, 50)
        inputs[2][0] = 'O'
    elif square == 3:
        center = Point(50, 150)
        inputs[0][1] = 'O'
    elif square == 4:
        center = Point(150, 150)
        inputs[1][1] = 'O'
    elif square == 5:
        center = Point(250, 150)
        inputs[2][1] = 'O'
    elif square == 6:
        center = Point(50, 250)
        inputs[0][2] = 'O'
    elif square == 7:
        center = Point(150, 250)
        inputs[1][2] = 'O'
    elif square == 8:
        center = Point(250, 250)
        inputs[2][2] = 'O'
    # Draw circle
    draw_circle(center)

    
def playerX(inputs, window, Xx, Xy): # Player X Place 
    square = get_square(Xx, Xy)
    print('square: ' + str(square))
    if square == 0:
        inputs[0][0] = 'X'
        diag1 = Line(Point(0, 0), Point(100, 100))
        diag2 = Line(Point(0, 100), Point(100, 0))
    elif square == 1:
        inputs[1][0] = 'X'
        diag1 = Line(Point(100, 0), Point(200, 100))
        diag2 = Line(Point(100, 100), Point(200, 0))
    elif square == 2:
        inputs[2][0] = 'X'
        diag1 = Line(Point(200, 0), Point(300, 100))
        diag2 = Line(Point(200, 100), Point(300, 0))
    elif square == 3:
        inputs[0][1] = 'X'
        diag1 = Line(Point(0, 100), Point(100, 200))
        diag2 = Line(Point(0, 200), Point(100, 100))
    elif square == 4:
        inputs[1][1] = 'X'
        diag1 = Line(Point(100, 100), Point(200, 200))
        diag2 = Line(Point(100, 200), Point(200, 100))
    elif square == 5:
        inputs[2][1] = 'X'
        diag1 = Line(Point(200, 100), Point(300, 200))
        diag2 = Line(Point(200, 200), Point(300, 100))
    elif square == 6:
        inputs[0][2] = 'X'
        diag1 = Line(Point(0, 200), Point(100, 300))
        diag2 = Line(Point(0, 300), Point(100, 200))
    elif square == 7:
        inputs[1][2] = 'X'
        diag1 = Line(Point(100, 200), Point(200, 300))
        diag2 = Line(Point(100, 300), Point(200, 200))
    elif square == 8:
        inputs[2][2] = 'X'
        diag1 = Line(Point(200, 200), Point(300, 300))
        diag2 = Line(Point(200, 300), Point(300, 200))
    # Draw X
    draw_x(diag1, diag2)


def check_win(inputs):
# Check if X won
    if inputs[0][0] == 'X' and inputs[0][1] == 'X' and inputs[0][2] == 'X':
        line = Line(Point(50,0), Point(50,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[1][0] == 'X' and inputs[1][1] == 'X' and inputs[1][2] == 'X':
        line = Line(Point(150,0), Point(150,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[2][0] == 'X' and inputs[2][1] == 'X' and inputs[2][2] == 'X':
        line = Line(Point(250,0), Point(250,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][0] == 'X' and inputs[1][0] == 'X' and inputs[2][0] == 'X':
        line = Line(Point(0,50), Point(300,50))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][1] == 'X' and inputs[1][1] == 'X' and inputs[2][1] == 'X':
        line = Line(Point(0,150), Point(300,150))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][2] == 'X' and inputs[1][2] == 'X' and inputs[2][2] == 'X':
        line = Line(Point(0,250), Point(300,250))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][0] == 'X' and inputs[1][1] == 'X' and inputs[2][2] == 'X':
        line = Line(Point(0,0), Point(300,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][2] == 'X' and inputs[1][1] == 'X' and inputs[2][0] == 'X':
        line = Line(Point(0,300), Point(300,0))
        line.setWidth(5)
        line.draw(window)
        return True
# Check if O won
    elif inputs[0][0] == 'O' and inputs[0][1] == 'O' and inputs[0][2] == 'O':
        line = Line(Point(50,0), Point(50,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[1][0] == 'O' and inputs[1][1] == 'O' and inputs[1][2] == 'O':
        line = Line(Point(150,0), Point(150,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[2][0] == 'O' and inputs[2][1] == 'O' and inputs[2][2] == 'O':
        line = Line(Point(250,0), Point(250,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][0] == 'O' and inputs[1][0] == 'O' and inputs[2][0] == 'O':
        line = Line(Point(0,50), Point(300,50))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][1] == 'O' and inputs[1][1] == 'O' and inputs[2][1] == 'O':
        line = Line(Point(0,150), Point(300,150))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][2] == 'O' and inputs[1][2] == 'O' and inputs[2][2] == 'O':
        line = Line(Point(0,250), Point(300,250))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][0] == 'O' and inputs[1][1] == 'O' and inputs[2][2] == 'O':
        line = Line(Point(0,0), Point(300,300))
        line.setWidth(5)
        line.draw(window)
        return True
    elif inputs[0][2] == 'O' and inputs[1][1] == 'O' and inputs[2][0] == 'O':
        line = Line(Point(0,300), Point(300,0))
        line.setWidth(5)
        line.draw(window)
        return True
    else:
        print('Tie!')

#while True:
show_window()