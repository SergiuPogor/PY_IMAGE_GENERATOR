from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create new image
image = generate_image(width=width, height=height, color=(255, 255, 255))
draw = ImageDraw.Draw(image)

# Number of shapes to generate
num_shapes = random.randint(100, 1000)

for i in range(num_shapes):
    # Random position and size
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(10, 100)

    # Random color
    color = generate_random_color()

    # Draw shape
    shape = random.randint(0, 2)
    if shape == 0:  # Triangle
        points = [(x - size, y + size), (x + size, y + size), (x, y - size)]
        draw.polygon(points, fill=color)
    elif shape == 1:  # Rectangle
        points = [(x - size, y - size), (x + size, y - size), (x + size, y + size), (x - size, y + size)]
        draw.polygon(points, fill=color)
    else:  # Circle
        draw.ellipse((x - size, y - size, x + size, y + size), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
