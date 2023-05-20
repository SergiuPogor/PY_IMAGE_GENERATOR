from noise import pnoise2

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic using Perlin noise algorithm
octaves = 4
persistence = 0.5
scale = 100.0

for x in range(width):
    for y in range(height):
        value = pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence)
        color = int((value + 1) / 2 * 255)
        draw.point((x, y), fill=(color, color, color))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
