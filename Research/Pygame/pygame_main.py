import pygame
from pygame.locals import *
from Research.Pygame.consts import *
from Research.Pygame.game_over import game_over
from Research.Pygame.keyboard_navigation import keyboard_navigation, choose_way
from Research.Pygame.utils import rockets_creator


# TODO Rewrite all for OOP
# TODO Research for python package managers
pygame.init()
pygame.display.set_caption('Snake')

playground = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))

x = int(DISPLAY_SIZE/2)
y = int(DISPLAY_SIZE/2)
r = 20
speed = 1
reverted = False
rockets = []
motion = K_LEFT
can_shoot = True
val = 0

while True:
    playground.fill(PINK)  # After every FPS tick, redraw background to black
    val += pygame.time.delay(FPS)  # FPS imitation
    if (val % 400) == 0 and not can_shoot:
        can_shoot = True
    # Draw rockets
    rockets_creator(rockets, playground)
    pygame.draw.circle(playground, BLUE, (x, y), r)  # draw circle
    pygame.Rect((30, 30, 30, 30))
    pygame.display.update()  # This require to redraw owr figures
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            exit()
        elif i.type == KEYDOWN:
            # Rockets push
            if i.key == K_SPACE and can_shoot:
                rockets.append([x - r/2, y - r/2])
                can_shoot = False

    x, y, motion = keyboard_navigation(x, y, speed, motion)
    # Make static moving for main obj
    x, y, motion = choose_way(x, y, speed, motion)
    # Checking borders
    if x <= 0 - r:
        game_over(playground)
        x = DISPLAY_SIZE
    elif x >= DISPLAY_SIZE + r:
        x = 0
    elif y <= 0 - r:
        y = DISPLAY_SIZE
    elif y >= DISPLAY_SIZE + r:
        y = 0

