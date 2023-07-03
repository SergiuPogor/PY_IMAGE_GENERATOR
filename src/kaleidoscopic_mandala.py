import math

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Define parameters for Mandala design
num_points = random.randint(10, 40)
radius = width / 2
angle_increment = 2 * math.pi / num_points

# Draw Mandala design
for i in range(num_points):
    x = center_x + radius * math.cos(i * angle_increment)
    y = center_y + radius * math.sin(i * angle_increment)
    for j in range(i + 1, num_points):
        x2 = center_x + radius * math.cos(j * angle_increment)
        y2 = center_y + radius * math.sin(j * angle_increment)
        draw.line((x, y, x2, y2), fill=generate_random_color(), width=random.randint(5, 10))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
