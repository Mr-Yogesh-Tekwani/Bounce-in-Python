import pygame
from Colors import *


class Label:
    def __init__(self, text, x, y, color, size):
        self.text = str(text)
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont('butch', size)
        self.text_id = self.font.render(self.text, True, self.color)

    def draw_label(self, s):
        s.game_display.blit(self.text_id, (self.x, self.y))
