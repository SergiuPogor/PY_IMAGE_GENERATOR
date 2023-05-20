from main import *

# Image size
width = 800
height = 600

image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Define the shapes and colors
shapes = ['rectangle', 'triangle', 'circle']
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Draw the shapes in a repeating pattern
for i in range(0, height, 50):
    for j in range(0, width, 50):
        shape = shapes[(i + j) % len(shapes)]
        color = colors[(i + j) % len(colors)]
        if shape == 'rectangle':
            draw.rectangle((j, i, j + 50, i + 50), fill=color)
        elif shape == 'triangle':
            draw.polygon([(j + 25, i), (j, i + 50), (j + 50, i + 50)], fill=color)
        elif shape == 'circle':
            draw.ellipse((j, i, j + 50, i + 50), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
