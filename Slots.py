import pygame
import random
from Colors import *


class Slots:
    def __init__(self,start_x,start_y,end_x,end_y,number):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.number = number
        self.slot_id = None

    def draw_slot(self,s):
        self.slot_id = pygame.draw.line(s.game_display,white,(self.end_x,self.end_y),(self.end_x,766),5)
        text = str(self.number)
        font = pygame.font.SysFont('butch',70)
        text = font.render(text, True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        x = (self.end_x + self.start_x) // 2 - 50
        y = self.end_y + 20
        s.game_display.blit(text, (x, y))

    def refresh_slot(self):
        pygame.display.update(self.slot_id)