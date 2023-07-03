import math

from main import *

# Image size
width = 600
height = 600

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic here
radius = 200
circles = 8
lines = 50
line_length = 100

for i in range(lines):
    angle = math.radians(i * (360 / lines))
    x = radius * math.cos(angle) + center_x
    y = radius * math.sin(angle) + center_y

    draw.line([(x, y), (center_x, center_y)], (0, 0, 255, 255), width=2)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
