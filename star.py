import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magical Floating Stars ✨")

# Colors
colors = [(255, 255, 255), (255, 215, 0), (173, 216, 230), (255, 182, 193)]

# Star positions
stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(50)]

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 20))  # Dark night background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, random.choice(colors), star, 3)
        star[1] -= 1  # Move star up
        if star[1] < 0:
            star[1] = HEIGHT
            star[0] = random.randint(0, WIDTH)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
