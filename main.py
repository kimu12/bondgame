# Import the pygame library and initialise the game engine
import pygame, sys
from sprite import *
from random import randint
pygame.init()




# Game Screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Practice window")

# Font stuff (under contruction)
font = pygame.font.Font('freesansbold.ttf', 32)

# Define colors
lgt_blue = (61, 226, 245)
lgt_red = (232, 72, 72)
background_green = (203, 247, 233)
purple  = (235, 126, 239)
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

#This will be a list that will contain all the sprites for our game.
ion_sprites_group = pygame.sprite.Group()

ion_1xy = (randint(60, 940), randint(10, 900))

ion_plus_1 = Ion_sprite(1, ion_1xy[0], ion_1xy[1]), Cat_puzzle(1, ion_1xy[0], ion_1xy[1])
ion_sprites_group.add(ion_plus_1)

ion_neg_2 = Ion_sprite(-2, 300, 300), An_puzzle(-2, 300, 300)
ion_sprites_group.add(ion_neg_2)

ion_plus_3 = Ion_sprite(-3, 300, 100)




# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

    # --- Game logic should go here
        #ion_sprites_group.update()

    # --- Drawing code should go here
        screen.fill(background_green)

    # Draw sprites  <-- this isn't working
        ion_sprites_group.draw(screen)

        #this is not a class object:
        pygame.draw.rect(screen, lgt_red, (100, 200, 60, 40))
        pygame.draw.rect(screen, background_green, (140, 210, 20, 20))
    #text = font.render('Na+', True, WHITE)

        pygame.display.flip()
    #pygame.display.blit(text)





    # --- Limit to 60 frames per second
        clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
