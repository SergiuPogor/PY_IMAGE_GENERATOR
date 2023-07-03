from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Draw liquid-like wavy and flowing shapes
for x in range(0, width, 5):
    for y in range(0, height, 5):
        dx = x + 5 * random.random() - 2.5
        dy = y + 5 * random.random() - 2.5
        draw.line([(x, y), (dx, dy)], fill=generate_random_color(), width=7
                  )

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
