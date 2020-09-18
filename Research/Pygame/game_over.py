import pygame

from Research.Pygame.consts import GOLD, CENTER_POS, FONT_NAME


def game_over(playground):
    font = pygame.font.Font(FONT_NAME, 30)
    text_surface = font.render("GAME OVER", True, GOLD)
    text_rect = text_surface.get_rect()
    text_rect.center = CENTER_POS
    playground.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.wait(5000)
