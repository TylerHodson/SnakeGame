# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()

grid_size = 50
grids_xy = 10

screen = pygame.display.set_mode(((grid_size * grids_xy), (grid_size * grids_xy)))
clock = pygame.time.Clock()
running = True
dt = 0
apple_x = random.randint(10, screen.get_width())
apple_y = random.randint(10, screen.get_height())
score = 0
banner_font = pygame.font.SysFont("Arial", 36)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple_pos = pygame.Vector2(apple_x, apple_y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", apple_pos, 10)
    pygame.draw.circle(screen, "green", player_pos, 15)


    # Create a text surface
    text_surface = banner_font.render(f'Score: {score}', True, (255, 255, 255))  # White color
    screen.blit(text_surface, (screen.get_width() / 2 - text_surface.get_width() / 2, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1 * grid_size
    if keys[pygame.K_s]:
        player_pos.y += 1 * grid_size
    if keys[pygame.K_a]:
        player_pos.x -= 1 * grid_size
    if keys[pygame.K_d]:
        player_pos.x += 1 * grid_size


    if player_pos.distance_to(apple_pos) < 25:
        score += 1
        apple_x = random.randint(10, screen.get_width())
        apple_y = random.randint(10, screen.get_height())
        apple_pos = pygame.Vector2(apple_x, apple_y)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000

pygame.quit()