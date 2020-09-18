import pygame
from pygame.locals import *
from Research.Pygame.consts import *
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

while True:
    playground.fill(BLACK)  # After every FPS tick, redraw background to black
    pygame.time.delay(FPS)  # FPS imitation
    # Draw rockets
    rockets_creator(rockets, playground)
    pygame.draw.circle(playground, BLUE, (x, y), r)  # draw circle
    pygame.display.update()  # This require to redraw owr figures
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            exit()
        elif i.type == KEYDOWN:
            # Rockets push
            if i.key == K_SPACE:
                rockets.append([x - r/2, y - r/2])

    x, y, motion = keyboard_navigation(x, y, speed, motion)
    # Make static moving for main obj
    x, y, motion = choose_way(x, y, speed, motion)
    # Checking borders
    if x <= 0 - r:
        x = DISPLAY_SIZE
    elif x >= DISPLAY_SIZE + r:
        x = 0
    elif y <= 0 - r:
        y = DISPLAY_SIZE
    elif y >= DISPLAY_SIZE + r:
        y = 0

