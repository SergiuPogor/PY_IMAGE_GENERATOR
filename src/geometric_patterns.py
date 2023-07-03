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

# Algorithm logic here
num_squares = random.randint(20, 100)
square_size = random.randint(20, 100)

for i in range(num_squares):
    angle = math.radians(i * 360 / num_squares)
    x = int(center_x + math.sin(angle) * center_x)
    y = int(center_y + math.cos(angle) * center_y)
    rect = [(x - square_size // 2, y - square_size // 2), (x + square_size // 2, y + square_size // 2)]
    draw.rectangle(rect, fill=generate_random_color(), outline=None)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
