from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Algorithm logic
num_brush_strokes = 1000
brush_radius = 5

for _ in range(num_brush_strokes):
    # Generate a random position around the central point
    x = random.randint(center_x - width // 4, center_x + width // 4)
    y = random.randint(center_y - height // 4, center_y + height // 4)

    # Generate a random shade of gray
    gray_level = random.randint(200, 255)
    color = (gray_level, gray_level, gray_level)

    # Draw a soft brush stroke
    draw.ellipse([(x - brush_radius, y - brush_radius), (x + brush_radius, y + brush_radius)], fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
