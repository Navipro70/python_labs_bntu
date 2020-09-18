from pygame import key
from Research.Pygame.consts import *
from pygame.locals import *


# Basic iteration for navigational system, that's return current
def keyboard_navigation(x, y, speed, motion):
    keys = key.get_pressed()
    if keys[K_LEFT] and keys[K_UP]:
        x -= speed
        y -= speed
        motion = K_LEFT_UP
    elif keys[K_LEFT] and keys[K_DOWN]:
        x -= speed
        y += speed
        motion = K_LEFT_DOWN
    elif keys[K_RIGHT] and keys[K_UP]:
        x += speed
        y -= speed
        motion = K_RIGHT_UP
    elif keys[K_RIGHT] and keys[K_DOWN]:
        x += speed
        y += speed
        motion = K_RIGHT_DOWN
    elif keys[K_LEFT]:
        x -= speed
        motion = K_LEFT
    elif keys[K_UP]:
        y -= speed
        motion = K_UP
    elif keys[K_RIGHT]:
        x += speed
        motion = K_RIGHT
    elif keys[K_DOWN]:
        y += speed
        motion = K_DOWN
    return x, y, motion


def choose_way(x, y, speed, motion):
    if motion == K_LEFT:
        x -= speed
    elif motion == K_UP:
        y -= speed
    elif motion == K_RIGHT:
        x += speed
    elif motion == K_DOWN:
        y += speed
    elif motion == K_LEFT_UP:
        x -= speed
        y -= speed
    elif motion == K_LEFT_DOWN:
        x -= speed
        y += speed
    elif motion == K_RIGHT_UP:
        x += speed
        y -= speed
    elif motion == K_RIGHT_DOWN:
        x += speed
        y += speed

    return x, y, motion
