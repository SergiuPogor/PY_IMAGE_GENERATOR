from random import randint

from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic here
for y in range(height):
    for x in range(width):
        dist_x = abs(x - center_x)
        dist_y = abs(y - center_y)
        warp_x = x + randint(-50, 50)
        warp_y = y + randint(-50, 50)
        if warp_x < 0:
            warp_x = 0
        elif warp_x >= width:
            warp_x = width - 1
        if warp_y < 0:
            warp_y = 0
        elif warp_y >= height:
            warp_y = height - 1
        src_pixel = image.getpixel((warp_x, warp_y))
        draw.point((x, y), fill=src_pixel)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
