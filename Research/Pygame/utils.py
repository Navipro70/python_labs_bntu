from pygame import draw

from Research.Pygame.consts import WHITE


def rockets_creator(rockets, playground):
    for index, rocket in enumerate(rockets):
        # 0 - x, 1 - y
        rocket[1] -= 10
        if rocket[1] < 0:
            del rockets[index]
            continue
        draw.rect(playground, WHITE, rocket + [20, 20])
