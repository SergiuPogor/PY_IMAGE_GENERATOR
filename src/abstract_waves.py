import math

from main import *

# Image size
width = 5000
height = 5000

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Algorithm logic here
num_waves = random.randint(5, 30)
amplitude_range = range(5, 30)
stroke_width_range = range(1, 5)

for i in range(num_waves):
    # generate random parameters
    amplitude = random.choice(amplitude_range)
    wavelength = random.randint(100, 300)
    stroke_width = random.choice(stroke_width_range)
    offset = random.randint(0, 360)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)

    # draw wave
    for x in range(WIDTH):
        y = center_y + amplitude * math.sin(x / wavelength * 2 * math.pi + offset)
        draw.line((x, y, x + 1, y), fill=color, width=stroke_width)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

