import pygame
from main import screen
"""
#This is from TicTacToe
class Text:
    def __init__(self, screen, x, y, text="", font_size=20):
        self.font = pygame.font.SysFont('leelawadee', font_size)
        self.screen = screen
        self.text = text
        self.pos = (x, y)

    def setText(self, text):
        self.text = text

    def draw(self):
        textsurface = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(textsurface, self.pos)
"""
BLACK = (0, 0, 0)

class Text:
    def __init__(self, text_string, font_size, pos_x, pos_y):
        self.text_string = text_string
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y

        #FIXME: should all these variables have 'self' infront of them?
        font_name = pygame.font.match_font('arial', 'bold')
        font = pygame.font.Font(font_name, font_size)
        text_surface = font.render(text_string, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (pos_x, pos_y)
        screen.blit(text_surface, text_rect)

