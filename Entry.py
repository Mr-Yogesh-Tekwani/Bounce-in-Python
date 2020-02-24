from main import *
from Colors import *


class Entry:
    def __init__(self, x, y, w, h, text=''):
        self.entry = pygame.Rect(x, y, w, h)
        self.text = text
        self.active_color = green
        self.inactive_color = blue
        self.font = pygame.font.SysFont(None, 30)
        self.text_id = self.font.render(text, True, blue)
        self.active = False
        self.color = self.inactive_color

    def resize(self):
        width = max(200, self.text_id.get_width() + 10)
        self.entry.w = width

    def draw(self, screen):
        self.color = self.active_color if self.active else self.inactive_color
        screen.blit(self.text_id, (self.entry.x + 5, self.entry.y + 5))
        pygame.draw.rect(screen, self.color, self.entry, 2)

    def type(self,event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_id = self.font.render(self.text, True, self.color)