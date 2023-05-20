import math

from main import *

# Set constants for the repetitive pattern
block_size = 300
num_blocks = 10
angle_increment = 5

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Loop through patterns at different angles
for angle in range(0, 360, angle_increment):

    # Calculate the vector from the center to a point on the circumference
    vector_x = math.cos(math.radians(angle))
    vector_y = math.sin(math.radians(angle))

    # Draw the pattern using blocks
    for i in range(num_blocks):
        for j in range(num_blocks):
            x = center_x - ((num_blocks - 1) * block_size / 2) + (i * block_size)
            y = center_y - ((num_blocks - 1) * block_size / 2) + (j * block_size)

            # Calculate the dot product of the vector with a vector from center to current block
            dot_product = (vector_x * (x - center_x)) + (vector_y * (y - center_y))

            # Calculate the opacity based on dot product
            opacity = int(255 * abs(dot_product) / ((num_blocks * block_size) / 2))

            # Draw the block
            draw.rectangle([(x, y), (x + block_size, y + block_size)], fill=(0, 0, 0, opacity))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
