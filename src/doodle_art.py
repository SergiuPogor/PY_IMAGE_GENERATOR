from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Draw random shapes and lines
for i in range(random.randint(500, 1000)):

    # Set up pen settings
    pen_color = generate_random_color()
    pen_width = random.randint(5, 20)

    x = random.randint(0, width)
    y = random.randint(0, height)
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    r = random.randint(10, 50)
    shape_type = random.choice(["line", "rectangle", "circle"])

    if shape_type == "line":
        draw.line((x, y, x1, y1), fill=pen_color, width=pen_width)
    elif shape_type == "rectangle":
        draw.rectangle((x, y, x + r, y + r), outline=pen_color)
    elif shape_type == "circle":
        draw.ellipse((x - r, y - r, x + r, y + r), outline=pen_color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
