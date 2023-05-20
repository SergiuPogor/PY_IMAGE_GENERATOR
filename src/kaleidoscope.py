import math

from main import *

# Example usage
width = WIDTH
height = HEIGHT

image = generate_image(width, height)
draw = ImageDraw.Draw(image)

# Define the shape parameters
shape_radius = width / 5
num_reflections = random.randint(10, 100)  # Number of reflections around the central point

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Draw the shape and its reflections
for i in range(num_reflections + 1):

    angle = i * (360 / num_reflections)

    # Calculate the position of the shape based on the angle
    x = center_x + int(shape_radius * math.cos(math.radians(angle)))
    y = center_y + int(shape_radius * math.sin(math.radians(angle)))

    # Draw the shape
    draw.ellipse([(x - shape_radius, y - shape_radius), (x + shape_radius, y + shape_radius)], generate_random_color())

    # Reflect the shape horizontally
    draw.ellipse([(center_x - (x - center_x), y - shape_radius), (center_x + (center_x - x), y + shape_radius)], generate_random_color())

    # Reflect the shape vertically
    draw.ellipse([(x - shape_radius, center_y - (y - center_y)), (x + shape_radius, center_y + (center_y - y))], generate_random_color())

    # Reflect the shape diagonally
    draw.ellipse([(center_x - (x - center_x), center_y - (y - center_y)), (center_x + (center_x - x), center_y + (center_y - y))], generate_random_color())

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
