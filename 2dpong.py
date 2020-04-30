import pygame
from sys import exit
from time import sleep
from random import randint, choice
import threading

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Player Scores
score_p1 = 0
score_p2 = 0
# Coordinates
ball_x = 700
ball_y = 350
ball_speed = 4
ball_vertical = 0
ball_horizontal = 0
# Player coordinates
p1_x = 690
p1_y = 350
p2_x = 0
p2_y = 350
# Pygame Window & Update Clock
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 750))
pygame.display.set_caption(f'2D Pong | Player 1: {score_p1} | Player 2: {score_p2}')
pygame.init()

# Draw ball


def pong_ball():
    global ball_x, ball_y, p2_x, p2_y
    pygame.draw.ellipse(screen, WHITE, [ball_x, ball_y, 15, 15])
# Draw players


def pong_sprite(color, y):
    if color == GREEN:
        pygame.draw.rect(screen, GREEN, [p1_x, y, 10, 150])
    elif color == RED:
        pygame.draw.rect(screen, RED, [p2_x, y, 10, 150])
    else:
        return 'Error'
# Move ball


def move_ball():
    global ball_x, ball_y, ball_speed, ball_vertical, ball_horizontal
    if ball_horizontal == 0:
        ball_x -= ball_speed
    if ball_vertical == 0:
        ball_y += ball_speed
        if ball_y > 690:
            ball_vertical = 1
    if ball_horizontal:
        ball_x += ball_speed
    if ball_vertical:
        ball_y -= ball_speed
        if ball_y < ball_speed:
            ball_vertical = 0
# Restart


def restart():
		global score_p1, score_p2
		score_p2 += 1 # //////////////////////////// to do:  detect if hit p1/p2
		pygame.display.set_caption(f'2D Pong | Player 1: {score_p1} | Player 2: {score_p2}')
# Main collision system


def main(): # Collision not really working
    global p1_x, p1_y, p2_x, p2_y, ball_x, ball_y, ball_horizontal, ball_vertical, score_p1, score_p2, mouse_x, mouse_y
    if ball_horizontal:
        if ball_x > 690:
            if ball_y > mouse_y and ball_y < mouse_y + 70:
                ball_horizontal = 0
            else:
                ball_x = 10
                ball_y = 20
                restart()
                pygame.display.update()
                pygame.time.delay(30)
    else:
        if ball_x < 10:
            if ball_y > p2_y and ball_y < p2_y + 70:
                ball_horizontal = 1
            else:
                ball_x = 690
                ball_y = 20
                restart()
                pygame.display.update()
                pygame.time.delay(30)


# Move p2
def move_p2():
    global p2_y
    if choice([True, False]) == True:
        p2_y += randint(100, 350)
    else:
        p2_y -= randint(75, 205)


running = True
p2_timer = threading.Timer(1.0, move_p2)
p2_timer.start()
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    move_ball()
    pong_ball()
    pong_sprite(GREEN, mouse_y) #P1
    pong_sprite(RED, p2_y) # P2
    main()
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)