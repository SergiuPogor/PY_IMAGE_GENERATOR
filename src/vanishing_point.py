from main import *

# Image size
width = WIDTH
height = HEIGHT

image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Draw lines converging towards the center point
for i in range(0, width, 50):
    draw.line([(i, 0), (center_x, center_y)], fill=(0, 0, 0))
    draw.line([(i, height), (center_x, center_y)], fill=(0, 0, 0))

for i in range(0, height, 50):
    draw.line([(0, i), (center_x, center_y)], fill=(0, 0, 0))
    draw.line([(width, i), (center_x, center_y)], fill=(0, 0, 0))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
