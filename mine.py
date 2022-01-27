import pygame, sys


class My_Group(pygame.sprite.Group):
    def __init__(self, pos_x, pos_y, id):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id


class My_Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, off_x, off_y, color, group_id):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = group_id
        self.offset_x = off_x
        self.offset_y = off_y

    def update(self):
        self.rect.center = (self.pos_x, self.pos_y)


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


my_groups = []

my_group_1 = My_Group(100, 100, 1)
my_sprite_1 = My_Sprite(50, 50, 100, 100, 0, 0, (128, 128, 0), 1)
my_sprite_2 = My_Sprite(50, 50, 150, 100, 50, 0, (128, 0, 0), 1)
my_group_1.add(my_sprite_1)
my_group_1.add(my_sprite_2)

my_groups.append(my_group_1)

my_group_2 = My_Group(500, 130, 2)
my_sprite = My_Sprite(50, 50, 500, 130, 0, 0, (0, 128, 200), 2)
my_group_2.add(my_sprite)

my_groups.append(my_group_2)

selected = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for group in my_groups:
                    for i, puzzle_piece in enumerate(group):
                        if puzzle_piece.rect.collidepoint(event.pos):
                            selected = puzzle_piece.id
                            selected_offset_x = puzzle_piece.pos_x - puzzle_piece.offset_x - event.pos[0]
                            selected_offset_y = puzzle_piece.pos_y - puzzle_piece.offset_y - event.pos[1]
                            print("selected", selected, selected_offset_x, selected_offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:
                for group in my_groups:
                    if group.id == selected:
                        for i, puzzle_piece in enumerate(group):
                            puzzle_piece.pos_x = event.pos[0] + selected_offset_x + puzzle_piece.offset_x
                            puzzle_piece.pos_y = event.pos[1] + selected_offset_y + puzzle_piece.offset_y

    screen.fill((0, 0, 0))
    for group in my_groups:
        group.update()
        group.draw(screen)

    pygame.display.flip()
    clock.tick(60)
