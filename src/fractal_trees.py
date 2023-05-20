import math

from main import *


def draw_tree(x1, y1, angle, length, level):
    if level > 0:
        # Calculate the endpoint of the branch
        x2 = x1 + int(math.cos(math.radians(angle)) * length)
        y2 = y1 + int(math.sin(math.radians(angle)) * length)

        # Draw the branch with a larger line width
        line_width = level // 2  # Adjust the line width based on the level
        draw.line([(x1, y1), (x2, y2)], tree_color, width=line_width)

        # Recursively draw smaller branches on each side
        draw_tree(x2, y2, angle - random.randint(20, 30), length * random.uniform(0.6, 0.8), level - 1)
        draw_tree(x2, y2, angle + random.randint(20, 30), length * random.uniform(0.6, 0.8), level - 1)


# Example usage
width = WIDTH
height = HEIGHT

image = generate_image(width, height)
draw = ImageDraw.Draw(image)

# Define the colors
tree_color = generate_random_color()

# Set the starting position and angle
start_x = width // 2
start_y = height - 500
start_angle = -90
start_length = 1000
start_level = 15

# Draw the fractal tree
draw_tree(start_x, start_y, start_angle, start_length, start_level)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
