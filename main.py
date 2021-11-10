# Import the pygame library and initialise the game engine
import pygame, sys
from sprite import Ion_sprite
from ions import generate_starting_pos
pygame.init()


# Game Screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("iBond Level 1")


# Define colors
lgt_blue = (61, 226, 245)
lgt_red = (232, 72, 72)
background_green = (203, 247, 233)
purple  = (235, 126, 239)
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

generate_starting_pos() #generates a semi-random list of starting positions for sprites

#This will be a list that will contain all the sprites for our game.
ion_sprites_group = pygame.sprite.Group()

ion_plus_1 = Ion_sprite(1, screen_width, screen_height, screen)
ion_sprites_group.add(ion_plus_1)
ion_sprites_group.add(ion_plus_1.group)

ion_plus_2 = Ion_sprite(2, screen_width, screen_height, screen)
ion_sprites_group.add(ion_plus_2)
ion_sprites_group.add(ion_plus_2.group)

ion_plus_3 = Ion_sprite(3, screen_width, screen_height, screen)
ion_sprites_group.add(ion_plus_3)
ion_sprites_group.add(ion_plus_3.group)

ion_neg_1 = Ion_sprite(-1, screen_width, screen_height, screen)
ion_sprites_group.add(ion_neg_1)
ion_sprites_group.add(ion_neg_1.group)

ion_neg_2 = Ion_sprite(-2, screen_width, screen_height, screen)
ion_sprites_group.add(ion_neg_2)
ion_sprites_group.add(ion_neg_2.group)

ion_neg_3 = Ion_sprite(-3, screen_width, screen_height, screen)
ion_sprites_group.add(ion_neg_3)
ion_sprites_group.add(ion_neg_3.group)



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

    # Draw sprites
        ion_sprites_group.draw(screen)

    # Write text
        #write_text(screen, 'IDK how to layer text onto sprite', 20, 200, 10)

        pygame.display.flip()
    #pygame.display.blit(text)



    # --- Limit to 60 frames per second
        clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
