import math

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(0, 0, 0, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic here
for i in range(0, 360, 15):
    x1 = center_x + int(50 * math.cos(math.radians(i)))
    y1 = center_y + int(50 * math.sin(math.radians(i)))
    x2 = center_x + int(150 * math.cos(math.radians(i)))
    y2 = center_y + int(150 * math.sin(math.radians(i)))
    draw.line((x1, y1, x2, y2), fill=(255, 255, 255, 255), width=3)

for i in range(0, 360, 30):
    x1 = center_x + int(75 * math.cos(math.radians(i)))
    y1 = center_y + int(75 * math.sin(math.radians(i)))
    x2 = center_x + int(125 * math.cos(math.radians(i)))
    y2 = center_y + int(125 * math.sin(math.radians(i)))
    draw.line((x1, y1, x2, y2), fill=(255, 0, 0, 255), width=2)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
