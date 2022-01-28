import pygame
from random import randint
from ions import rand_ion, starting_pos_lst

WHITE = (255, 255, 255)
RED = (255, 0 , 0)
BLACK = (0, 0, 0)
lgt_blue = (61, 226, 245)
lgt_red = (232, 72, 72)
background_green = (203, 247, 233)
width = 60


class Ion_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        #FIXME:  this movement code will only move all sprites.  It wont be adaptable for dynamic
        #drag & drop fuctionality since it is not part of the while loop running in main.py -MG 12/21
        self.click = False

    def update_offsets(self):
        for sprite in self:
            sprite.offset_x = 0
            sprite.offset_y = 0
            pass
'''
    def update(self):
        #print("hello") #debugging
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for sprite in self:
            if self.click:
                sprite.pos_x = mouse_x
                sprite.pos_y = mouse_y
                sprite.update()
                print("move")
'''


class Ion_sprite(pygame.sprite.Sprite):
    # This class represents ion puzzle piece sprite, and inherits from pygame's Sprite class

    def __init__(self, charge, screen_width, screen_height, screen):
        super().__init__()  # Calls parent class
        self.charge = charge
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        xy_pos = starting_pos_lst.pop(randint(0, len(starting_pos_lst)-1))
        self.pos_x = xy_pos[0]
        self.pos_y = xy_pos[1]
        self.offset_x = 0
        self.offset_y = 0

        if self.charge >= 0:
            color = lgt_red
        else:
            color = lgt_blue

        height = abs(self.charge)*40  #puzzle pieces are 60 wide by charge*40 long

        self.image = pygame.Surface([width, height]) #creates blank image
        self.image.fill(color) #fills blank image with color
        self.rect = self.image.get_rect()  #this draws rectangle around image from previous 2 lines
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.group = pygame.sprite.Group() #creats a group for the puzzle features.  Whole group can be drawn as if its one object
        ion_text = rand_ion(self.charge) #gets ion's text label
        #print(ion_text)  #debugging

        if self.charge >= 0:  #adds cation puzzle piece shape features
            y_shift = 10
            x_shift = 40
            for puz in range (abs(charge)):
                shifted_pos_y = self.pos_y + y_shift
                self.group.add(Cat_puzzle(self.pos_x + x_shift, shifted_pos_y, x_shift, y_shift))
                y_shift += 40
        else:  #adds anion puzzle piece shape features
            x_shift = -20
            y_shift = 10
            for puz in range(abs(charge)):
                shifted_pos_x = self.pos_x + x_shift
                shifted_pos_y = self.pos_y + y_shift
                self.group.add(An_puzzle(self.charge, shifted_pos_x, shifted_pos_y, x_shift, y_shift))
                y_shift += 40
        self.group.add(Text(ion_text, 25, BLACK, self.pos_x, self.pos_y, charge))

        for object in self.group: #self.group only contains puzzle features and text, should it also contain main rect sprite?
            print('{} {}'.format(object, type(object)))

    def update(self):
        self.rect.topleft = (self.pos_x, self.pos_y)
        '''
        if self.charge >= 0:
            print("Hey jude")
            y_shift = 10
            x_shift = 40
            for item in self.group:
                print("dont let me down")
                if type(item) is Cat_puzzle:
                    print("take a sad song")
                    shifted_pos_y = self.pos_y + y_shift
                    item.rect.topleft = (self.pos_x + x_shift, shifted_pos_y)
                    print("and make it better", item.rect.topleft)
                    y_shift += 40
                    item.update()
        else:
            x_shift = -20
            y_shift = 10
            for item in self.group:
                if type(item) is An_puzzle:
                    shifted_pos_x = self.pos_x + x_shift
                    shifted_pos_y = self.pos_y + y_shift
                    item.rect.topleft = (shifted_pos_x, shifted_pos_y)
                    y_shift += 40
                    item.update()
        '''

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, pos_x, pos_y, charge):
        super(Text, self).__init__() #why is the 'Text' here? can it just be 'super().__init__()'
        font_name = pygame.font.match_font('arial', 'bold')
        self.color = color
        self.font = pygame.font.Font(font_name, size)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set(text, charge)
        self.offset_x = 0
        self.offset_y = 0

    def set(self, text, charge):
        y_shift = abs(charge) * 20
        if charge < 0:
            x_shift = 30
        else:
            if len(text) == 1:
                x_shift = 20
            else:
                x_shift = 17
        self.image = self.font.render(str(text), 1, self.color) #font.render(text, antialias, color)
        self.rect = self.image.get_rect(center = (self.pos_x + x_shift, self.pos_y + y_shift))

    def update(self):
        self.rect.topleft = (self.pos_x, self.pos_y)

class Cat_puzzle(pygame.sprite.Sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, pos_x, pos_y, off_x, off_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface([20, 20])
        self.image.fill(background_green)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.offset_x = off_x
        self.offset_y = off_y

    def update(self):
        self.rect.topleft = (self.pos_x, self.pos_y)

class An_puzzle(pygame.sprite.Sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, charge, pos_x, pos_y, off_x, off_y):
        super().__init__()
        self.charge = charge
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface([20, 20])
        self.image.fill(lgt_blue)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.offset_x = off_x
        self.offset_y = off_y

    def update(self):
        self.rect.topleft = (self.pos_x, self.pos_y)

