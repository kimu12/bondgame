import pygame
from random import randint
from ions import rand_ion

WHITE = (255, 255, 255)
RED = (255, 0 , 0)
BLACK = (0, 0, 0)
lgt_blue = (61, 226, 245)
lgt_red = (232, 72, 72)
background_green = (203, 247, 233)
width = 60

def random_pos(screen_width, screen_height):
    x_buffer = 60
    y_top_buffer = 10
    y_bottom_buffer = 100
    xy_pos = (randint(x_buffer, screen_width - x_buffer), randint(y_top_buffer, screen_height - y_bottom_buffer))
    return xy_pos

class Ion_sprite(pygame.sprite.Sprite):
    # This class represents ion puzzle piece sprite, and inherits from pygame's Sprite class

    def __init__(self, charge, screen_width, screen_height, screen):
        super().__init__()  # Calls parent class
        self.charge = charge
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        xy_pos = random_pos(screen_width, screen_height)
        pos_x = xy_pos[0]
        pos_y = xy_pos[1]

        if self.charge >= 0:
            color = lgt_red
        else:
            color = lgt_blue

        height = abs(self.charge)*40

        self.image = pygame.Surface([width, height]) #creates blank image
        self.image.fill(color) #fills blank image with color
        self.rect = self.image.get_rect()  #this draws rectangle around image from previous 2 lines
        self.rect = [pos_x, pos_y]
        self.group = pygame.sprite.Group() #creats a group for the puzzle features.  Whole group can be drawn as if its one object
        ion_text = rand_ion(1)
        print(ion_text)
        #self.group.add(Sprite_text(charge, pos_x, pos_y, ion_text, screen))
        if self.charge >= 0:
            y_shift = 10
            x_shift = 40
            for puz in range (abs(charge)):
                shifted_pos_y = pos_y + y_shift
                self.group.add(Cat_puzzle(pos_x + x_shift, shifted_pos_y))
                y_shift += 40
        else:
            x_shift = -20
            y_shift = 10
            for puz in range(abs(charge)):
                shifted_pos_x = pos_x + x_shift
                shifted_pos_y = pos_y + y_shift
                self.group.add(An_puzzle(self.charge, shifted_pos_x, shifted_pos_y))
                y_shift += 40


class Cat_puzzle(pygame.sprite.Sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface([20, 20])
        self.image.fill(background_green)
        self.rect = self.image.get_rect()
        self.rect = [pos_x, pos_y]

class An_puzzle(pygame.sprite.Sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, charge, pos_x, pos_y):
        super().__init__()
        self.charge = charge
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface([20, 20])
        self.image.fill(lgt_blue)
        self.rect = self.image.get_rect()
        self.rect = [pos_x, pos_y]

class Sprite_text(pygame.sprite.Sprite): #FIXME: This creats a rect but no text shows :(
    #This class layers text onto the sprite
    def __init__(self, charge, pos_x, pos_y, text_string, screen):
        super().__init__()
        self.screen = screen
        self.charge = charge
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_string = text_string
        self.font_size = 20

        if self.charge > 0:
            fill_color = lgt_red
        else:
            fill_color = lgt_blue

        self.image = pygame.Surface([20, 20])
        self.image.fill(fill_color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.font_name = pygame.font.match_font('arial', 'bold')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.text_surface = self.font.render(self.text_string, True, BLACK)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (pos_x, pos_y)
        self.screen.blit(self.text_surface, self.text_rect)










