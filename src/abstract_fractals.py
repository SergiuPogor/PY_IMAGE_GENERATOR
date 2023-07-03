from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(255, 255, 255, 0))
draw = ImageDraw.Draw(image)


# Sierpinski Triangle algorithm
def sierpinski(x, y, size, depth):
    if depth == 0:
        draw.rectangle((x, y, x + size, y + size), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255))
    else:
        sierpinski(x, y, size // 2, depth - 1)
        sierpinski(x + size // 2, y, size // 2, depth - 1)
        sierpinski(x, y + size // 2, size // 2, depth - 1)


# Call the Sierpinski Triangle algorithm with depth=5
sierpinski(0, 0, width, 4)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
