import math

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Number of shapes to generate
num_shapes = random.randint(100, 1000)

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

for i in range(num_shapes):
    # Generate random number of sides
    sides = random.randint(3, 8)

    # Generate random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Generate random size and rotation
    size = random.randint(50, 200)
    rotation = random.randint(0, 360)

    # Generate random point for center of shape
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)

    # Generate vertices for polygon
    vertices = []
    for j in range(sides):
        angle = 2 * math.pi * j / sides + math.radians(rotation)
        vertex_x = x + size * math.cos(angle)
        vertex_y = y + size * math.sin(angle)
        vertices.append((vertex_x, vertex_y))

    # Draw polygon on image
    draw.polygon(vertices, fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
