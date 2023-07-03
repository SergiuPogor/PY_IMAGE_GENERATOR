from main import *

# Image size
width = WIDTH
height = HEIGHT

image = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Draw a symmetrical shape
shape = [(50, 50), (150, 50), (150, 150), (50, 150)]
draw.polygon(shape, fill=(255, 255, 255, 255))
# Reflect the shape horizontally
draw.polygon(list(map(lambda point: (WIDTH - point[0], point[1]), shape)), fill=(255, 255, 255, 255))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
