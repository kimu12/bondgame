import pygame
import sys

pygame.init()
# initialize pygame

clock = pygame.time.Clock()
# screen code
screen_width = 1000
screen_height = 1000

title_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("iBond")

# fonts/ constants
huge_text = pygame.font.SysFont("arial", 60)
big_font = pygame.font.SysFont("arial", 30)
reg_font = pygame.font.SysFont("arial", 14)
red = (252, 40, 3)
white = (255, 255, 255)
black = (0, 0, 0)
roy_blue = (3, 115, 252)

mantis = (112, 195, 109)
ong_yell = (241, 193, 34)
eng_vermill = (201, 68, 68)
myrt_green = (38, 116, 125)

#text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

# load images
image = pygame.image.load(r'/Users/nikratzlaff/Desktop/ibond.png')

# button function
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height >mouse[1] > y:
        pygame.draw.rect(title_screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(title_screen, defaultcolor, (x, y, width, height))



# start menu function
def start_menu():
    #start_text = big_font.render('iBond Game', True, black)

    while True:
        title_screen.fill((38, 116, 125))
        title_screen.blit(image, (0, 40))

        play_button = create_button((screen_width / 4), 650, 200, 100, eng_vermill, ong_yell)
        play_button_text = big_font.render("Start", True, black)
        title_screen.blit(play_button_text, ((screen_width / 4), 690, 200, 100))


        quit_button = create_button((screen_width / 2), 650, 200, 100, eng_vermill, ong_yell)
        quit_button_text = big_font.render("Quit", True, black)
        title_screen.blit(quit_button_text, ((screen_width / 2), 690, 200, 100))
        if quit_button:
                quit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
        return True



# game loop
while True:
    start_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




pygame.display.update()
clock.tick(15)