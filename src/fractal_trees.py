Here is an
example
code
to
generate
fractal
trees:

import math

from main import *

# Image size
width = 800
height = 800

image = generate_image(width=width, height=height, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2


# Fractal tree function
def fractal_tree(x, y, angle, depth):
    # Draw the trunk
    x2 = x + int(math.cos(math.radians(angle)) * depth * 10.0)
    y2 = y + int(math.sin(math.radians(angle)) * depth * 10.0)
    draw.line((x, y, x2, y2), fill=(255, 255, 255))

    # Recursively draw smaller branches
    if depth > 1:
        fractal_tree(x2, y2, angle - 20, depth - 1)
        fractal_tree(x2, y2, angle + 20, depth - 1)


# Call the fractal tree function
fractal_tree(center_x, center_y, -90, 9)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
