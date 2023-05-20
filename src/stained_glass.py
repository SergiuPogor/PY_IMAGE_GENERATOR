import random

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Color options with transparency
colors = [(255, 0, 0, 100), (0, 255, 0, 100), (0, 0, 255, 100)]

# Generating a white canvas
image = generate_image(width=width, height=height, color=(255, 255, 255, 255))

# Creating the drawing context
draw = ImageDraw.Draw(image)

# Creating shapes with random colors and black outlines
for x in range(0, width, 40):
    for y in range(0, height, 40):
        top_left = (x, y)
        bottom_right = (x + 40, y + 40)
        color = random.choice(colors)
        draw.rectangle([top_left, bottom_right], fill=color, outline=(0, 0, 0, 255))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
