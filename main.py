import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# BG colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# sprite class
class sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-3, 3), random.randint(-3, 3)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def change_background_function():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

all_sprite_list = pygame.sprite.Group()

sp1 = sprite(WHITE, 20, 20)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprite_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bouncing Sprite")
bg_color = BLUE
screen.fill(bg_color)

exit = False

clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_function()
        
    all_sprite_list.update()
    screen.fill(bg_color)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()