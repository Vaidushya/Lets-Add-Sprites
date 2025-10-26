import pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

clock = pygame.time.Clock()
player = pygame.Rect(100, 100, 60, 60)
enemy = pygame.Rect(400, 300, 100, 100)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    # controls
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    if player.colliderect(enemy):
        screen.fill(BLUE)
    else:
        screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()