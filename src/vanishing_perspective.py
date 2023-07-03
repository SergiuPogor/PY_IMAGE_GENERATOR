from main import *

# Image size
WIDTH = 800
HEIGHT = 600

image = Image.new('RGBA', (WIDTH, HEIGHT), color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Draw lines converging towards the center
num_lines = 10
line_len = 200
angle_step = 5

for i in range(num_lines):
    angle = i * angle_step
    x1 = center_x + line_len * (angle / 90)
    x2 = center_x - line_len * (angle / 90)
    draw.line([(x1, 0), (center_x, center_y), (x2, HEIGHT)], fill=(0, 0, 0))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
