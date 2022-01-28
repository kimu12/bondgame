# Import the pygame library and initialise the game engine
import pygame, sys

import sprite
from sprite import Ion_sprite, Ion_group
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

generate_starting_pos() #generates a semi-random list of starting positions for sprites so they don't overlap

#This will be a list that will contain all the sprites for our game.
# ion_sprites_group = pygame.sprite.Group()

ion_sprites_groups = []

ion_group_1 = Ion_group()
ion_plus = Ion_sprite(1, screen_width, screen_height, screen)
ion_group_1.add(ion_plus)
ion_group_1.add(ion_plus.group)

ion_sprites_groups.append(ion_group_1)

ion_group_2 = Ion_group()
ion_plus = Ion_sprite(2, screen_width, screen_height, screen)
ion_group_2.add(ion_plus)
ion_group_2.add(ion_plus.group)

ion_sprites_groups.append(ion_group_2)

ion_group_3 = Ion_group()
ion_plus = Ion_sprite(3, screen_width, screen_height, screen)
ion_group_3.add(ion_plus)
ion_group_3.add(ion_plus.group)

ion_sprites_groups.append(ion_group_3)

ion_group_4 = Ion_group()
ion_neg = Ion_sprite(-1, screen_width, screen_height, screen)
ion_group_4.add(ion_neg)
ion_group_4.add(ion_neg.group)

ion_sprites_groups.append(ion_group_4)

ion_group_5 = Ion_group()
ion_neg = Ion_sprite(-2, screen_width, screen_height, screen)
ion_group_5.add(ion_neg)
ion_group_5.add(ion_neg.group)

ion_sprites_groups.append(ion_group_5)

#FIXME:  there's an int getting added to ion_sprites_group here somehow
ion_group_6 = Ion_group()
ion_neg = Ion_sprite(-3, screen_width, screen_height, screen)
ion_group_6.add(ion_neg)
ion_group_6.add(ion_neg.group)

ion_sprites_groups.append(ion_group_6)

# for i, object in enumerate(ion_sprites_group):
    # if type(object) == int:
    # print('{}: {}, type: {}'.format(i+1, object, type(object)))

selected = None

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #FIXME: drag & drop code:
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: #'1' - Is left mousebutton being clicked?
            # for object in ion_sprites_group:
            #    print(type(object))
            #print (ion_sprites_group) --> this yields "<Group(24 sprites)>"
            #print (type(ion_sprites_group)) --> this yields "<class 'pygame.sprite.Group'>"
            #for i, puzzle_piece in enumerate(ion_sprites_group):
            for i, group in enumerate(ion_sprites_groups):
                for puzzle_piece in group:
                    #if type(puzzle_piece) != int: #Delete this 'if' statement line once the int is nolonger sneaking into ion_sprites_group
                    #FIXME: AttributeError: 'list' object has no attribute 'collidepoint': puzzle_piece.rect[1].collidepoint(event.pos):
                    #so this object is a list... when "puzzle_piece.rect[0].collidepoint(event.pos):", assuming 1st item in list is rect object...
                    #program closes 'Process finished with exit code 1' when clicking on sprite...
                    print(type(puzzle_piece))
                    if puzzle_piece.rect.collidepoint(event.pos):
                        selected = i
                        selected_offset_x = puzzle_piece.pos_x - event.pos[0]
                        selected_offset_y = puzzle_piece.pos_y - event.pos[1]

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            selected = None

    elif event.type == pygame.MOUSEMOTION:
        if selected is not None:  # selected can be `0` so `is not None` is required
            # move object
            #FIXME: Class 'Group' does not define '__getitem__', so the [] operator cannot be used on its instances
            print("to move")
            for piece in ion_sprites_groups[selected]:
                # if type(piece) is Ion_sprite or type(piece) is sprite.Text:
                print("moving", piece)
                piece.pos_x = event.pos[0] + selected_offset_x + piece.offset_x
                piece.pos_y = event.pos[1] + selected_offset_y + piece.offset_y
            print("moved")


    pygame.display.flip()

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(background_green)

    # Draw sprites
    for group in ion_sprites_groups:
        group.update()
        group.draw(screen)

    # Write text
    pygame.display.flip()




    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
