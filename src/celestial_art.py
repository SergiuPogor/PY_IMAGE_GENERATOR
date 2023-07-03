from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create a new image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

num_stars = random.randint(500, 10000)
for i in range(num_stars):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(10, 50)
    color = generate_random_color()
    draw.ellipse((x, y, x + size, y + size), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
