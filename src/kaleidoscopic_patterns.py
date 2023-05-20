from PIL import ImageDraw

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Design Element shape
radius = 100
sides = 5

# Reflect and Repeat the Design Element in a circular arrangement
for i in range(sides):
    angle = i * 2.0 * math.pi / sides
    x = center_x + int(radius * math.cos(angle))
    y = center_y + int(radius * math.sin(angle))

    polygon = [
        (center_x, center_y),
        (x, y),
        (center_x - (x - center_x), center_y - (y - center_y))
    ]
    draw.polygon(polygon, fill=(255, 255, 255, 50))

# Save Image to a local file
save_image_to_file(image, 'kaleidoscope.png')
