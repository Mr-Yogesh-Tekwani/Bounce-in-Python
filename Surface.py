import pygame

class Surface:
    def __init__(self, resolution, title, color=None):
        '''
        :param resolution: The size of window (width,height) as a tuple
        :param title: The name of the window
        :param color: background color of screen
        '''
        self.game_display = pygame.display.set_mode(resolution, pygame.RESIZABLE)
        self.screen = None
        pygame.display.set_caption(title)  # Title Of The Window
        self.screen_color = color

    def draw_surface(self):
        self.screen = self.game_display.fill(self.screen_color) # Filling the screen with given color

    def refresh_background(self):
        pygame.display.update(self.screen) # Updating the screen when new objects are added or removed
