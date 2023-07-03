import random

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic here
num_circles = 2000
circle_radius_range = (5, 30)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
density_range = (0.2, 0.5)

for i in range(num_circles):
    x = random.randint(0, width)
    y = random.randint(0, height)
    radius = random.randint(circle_radius_range[0], circle_radius_range[1])
    color = random.choice(colors)
    density = random.uniform(density_range[0], density_range[1])
    if random.random() < density:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
