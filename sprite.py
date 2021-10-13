import pygame

WHITE = (255, 255, 255)
lgt_blue = (61, 226, 245)
lgt_red = (232, 72, 72)
background_green = (203, 247, 233)
width = 60

class Ion_sprite(pygame.sprite.Sprite):
    # This class represents ion puzzle piece sprite, and inherits from pygame's Sprite class

    def __init__(self, charge, pos_x, pos_y):
        super().__init__()  # Calls parent class
        self.charge = charge
        self.pos_x = pos_x
        self.pos_y = pos_y
        if self.charge >= 0:
            color = lgt_red
        else:
            color = lgt_blue

        height = abs(self.charge)*40

        self.image = pygame.Surface([width, height]) #creates blank image
        self.image.fill(color) #fills blank image with color
        self.rect = self.image.get_rect()  #this draws rectangle around image from previous 2 lines
        self.rect.center = [pos_x, pos_y]

class Cat_puzzle(Ion_sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, charge, pos_x, pos_y):
        super().__init__(charge, pos_x, pos_y)

        if abs(charge) == 1:
            self.image = pygame.Surface([20, 20])
            self.image.fill(background_green)
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x+20, pos_y]

        if abs(charge) == 2:

            self.image = pygame.Surface([20, 20])
            self.image.fill(background_green)
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x + 20, pos_y-15]
            """
            block_y_pos = [285, 315]
            for y_pos in block_y_pos:
                self.image = pygame.Surface([20, 20])
                self.image.fill(background_green)
                self.rect = self.image.get_rect()
                self.rect.center = [pos_x + 20, block_y_pos]
            """
class An_puzzle(Ion_sprite):
    # This class layers a smaller rectangles to form puzzle pieces
    def __init__(self, charge, pos_x, pos_y):
        super().__init__(charge, pos_x, pos_y)

        if abs(charge) == 1:
            self.image = pygame.Surface([20, 20])
            self.image.fill(lgt_blue)
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x-40, pos_y]

        if abs(charge) == 2:

            self.image = pygame.Surface([20, 20])
            self.image.fill(lgt_blue)
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x-40, pos_y-15]







