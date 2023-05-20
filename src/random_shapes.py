import random

from main import *

# Example usage
width = WIDTH
height = HEIGHT

image = generate_image(width, height)

num_shapes = 200
min_shape_size = width / 100
max_shape_size = width / 10

border_size = 20

for _ in range(num_shapes):
    shape_type = random.choice(['circle', 'square', 'triangle'])
    shape_size = random.randint(min_shape_size, max_shape_size)
    shape_position = (random.randint(0, width), random.randint(0, height))
    shape_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    draw = ImageDraw.Draw(image)

    if shape_type == 'circle':
        bounding_box = [(shape_position[0] - shape_size, shape_position[1] - shape_size),
                        (shape_position[0] + shape_size, shape_position[1] + shape_size)]
        draw.ellipse(bounding_box, outline=shape_color, width=border_size)
    elif shape_type == 'square':
        bounding_box = [(shape_position[0] - shape_size, shape_position[1] - shape_size),
                        (shape_position[0] + shape_size, shape_position[1] + shape_size)]
        draw.rectangle(bounding_box, outline=shape_color, width=border_size)
    elif shape_type == 'triangle':
        x1, y1 = shape_position
        x2, y2 = x1 + shape_size, y1 + shape_size
        x3, y3 = x1 + shape_size, y1 - shape_size
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], outline=shape_color, width=border_size)

    del draw

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
