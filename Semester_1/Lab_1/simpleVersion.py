# This program is first lab in BNTU, designed to show basic capabilities of python.
# Version 1.0
# Full name: Matatov Dmitry Valer'evich, ФИО: Мататов Дмитрий Валерьевич
# Group number: № 10702120
# Date of development: 13 september, 2020
from tkinter import *  # Import all func and objects from GUI lib (tkinter)
import pygame
from pygame.locals import *
from Research.Pygame.consts import *

GAME_OVER = "" \
            "#########\t      #      \t#       #\t#######\n" \
            "#        \t     # #     \t# #   # #\t#      \n" \
            "#        \t    #   #    \t#  # #  #\t#######\n" \
            "#  ######\t   #######   \t#   #   #\t#      \n" \
            "#       #\t  #       #  \t#       #\t#      \n" \
            "#       #\t #         # \t#       #\t#      \n" \
            "#########\t#           #\t#       #\t#######\n" \
            "" \
            "#########\t#           #\t#########\t####### \n" \
            "#       #\t #         # \t#        \t#      #\n" \
            "#       #\t  #       #  \t#########\t#      #\n" \
            "#       #\t   #     #   \t#        \t####### \n" \
            "#       #\t    #   #    \t#        \t# #     \n" \
            "#       #\t     # #     \t#        \t#   #   \n" \
            "#########\t      #      \t#########\t#     # \n"

print('\n\n"Безнадёжно — это когда на крышку гроба падает земля. Остальное можно исправить. — Джейсон Стэтхэм"'
      '\n"Hopeless is when the earth falls on the lid of the coffin. The rest can be fixed. — Jason Statham"\n\n {0}'.format(
    GAME_OVER))

# TODO Rewrite all for OOP
# TODO Research for python package managers
pygame.init()
pygame.display.set_caption('Snake')

playground = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
font = pygame.font.Font('roboto.ttf', 40)
text = font.render(GAME_OVER, True, GOLD)

surface = pygame.Surface((240, 40))
surface.fill((255, 255, 255))
surface.blit(text, pygame.Rect(0, 0, 100, 100))
rerenders = 0
while True:
    playground.fill(BLACK)  # After every FPS tick, redraw background to black
    rerenders += FPS
    surface.set_alpha(rerenders/20)
    playground.blit(surface, pygame.Rect(0, 30, 10, 10))
    pygame.time.delay(FPS)  # FPS imitation
    pygame.display.update()  # This require to redraw owr figures
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            exit()

