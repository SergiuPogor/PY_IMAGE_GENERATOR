from math import cos, sin, radians

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Generate a black image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Draw a spiral in white color
angle = 0
radius = 0
for i in range(4000):
    x = width / 2 + radius * cos(radians(angle))
    y = height / 2 + radius * sin(radians(angle))
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=generate_random_color())
    angle += 4
    radius += 0.1

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
