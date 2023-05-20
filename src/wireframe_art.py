import pygame

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Initialize Pygame
pygame.init()

# Create a new Pygame surface
surface = pygame.Surface((width, height))

# Set the background color
background = (0, 0, 0)
surface.fill(background)

# Create a new Pygame draw object
draw = pygame.draw

# Draw a simple wireframe square at the center of the image
color = (255, 255, 255)
thickness = 2
x = width // 2 - 50
y = height // 2 - 50
size = 100
points = [(x, y), (x + size, y), (x + size, y + size), (x, y + size)]
draw.lines(surface, color, True, points, thickness)

# Save the image to a file
pygame.image.save(surface, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

# Cleanup Pygame
pygame.quit()
