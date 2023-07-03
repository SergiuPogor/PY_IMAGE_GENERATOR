from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create new image
image = generate_image(width=width, height=height, color=(255, 255, 255, 255))

# Create a draw object
draw = ImageDraw.Draw(image)

# Import random library
import random

# Set number of lines to generate
num_lines = 50

for i in range(num_lines):
    # Generate random start and end points for line
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)
    end_x = random.randint(0, width)
    end_y = random.randint(0, height)

    # Generate random color for line
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)

    # Draw line
    draw.line((start_x, start_y, end_x, end_y), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
