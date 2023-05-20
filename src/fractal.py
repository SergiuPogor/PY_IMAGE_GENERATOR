import math
import random

from main import *

# Example usage
width = WIDTH
height = HEIGHT

image = generate_image(width, height)

# center_x = width / 2
# center_y = height / 2
# circle_radius = 1000
# border_size = int(circle_radius / 100)
#
# num_circles = 100
# angle_step = 360 / num_circles

zoom = 1
max_iterations=1000

# Create a blank image with the specified dimensions
image = Image.new('RGB', (width, height))

# Define the range of the complex plane to map to the image dimensions
x_min, x_max = -2.0 / zoom, 2.0 / zoom
y_min, y_max = -2.0 / zoom, 2.0 / zoom

# Iterate over each pixel in the image
for x in range(width):
    for y in range(height):
        # Map pixel coordinates to complex plane
        zx = 1.5 * (x - width / 2) / (0.5 * zoom * width)
        zy = 1.0 * (y - height / 2) / (0.5 * zoom * height)

        c = complex(zx, zy)
        z = complex(0, 0)

        iteration = 0
        while abs(z) < 2 and iteration < max_iterations:
            z = z * z + c
            iteration += 1

        color = (iteration % 256, 0, 0)  # Adjust color based on iteration count

        image.putpixel((x, y), color)

# Define the file path with datetime as the name
final_filename = '{}/{}/{}.png'.format(MEDIA_PATH, APP_NAME, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
make_dir_if_not_exist(final_filename)

# Save the image
image.save(final_filename, "PNG")

print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + '{}'.format(final_filename))
