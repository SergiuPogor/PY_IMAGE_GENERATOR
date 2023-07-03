import math

from PIL import ImageFont, ImageFilter

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Possible characters to use for the graffiti
characters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Possible colors to use for the graffiti
# colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255)]
colors = []
for character in characters:
    colors.append(generate_random_color())


def generate_graffiti(characters, colors):
    # Randomly select a character and color for each letter
    graffiti = []
    for i in range(random.randint(5, 15)):
        character = random.choice(characters)
        color = random.choice(colors)
        graffiti.append((character, color))

    return graffiti


def draw_graffiti(graffiti):
    # Calculate the central point of the image
    center_x = width // 2
    center_y = height // 2

    # Set the font and initial size
    font_size = random.randint(100, 200)
    font = ImageFont.truetype('data/input/fonts/arial.ttf', font_size)

    # Draw each letter of the graffiti
    for i, (character, color) in enumerate(graffiti):
        # Calculate the position of the letter relative to the central point
        angle = random.uniform(-0.2, 0.2)
        radius = random.uniform(50, 150)
        x = int(center_x + radius * math.cos(angle + 2 * math.pi * i / len(graffiti))) - font_size / 2
        y = int(center_y + radius * math.sin(angle + 2 * math.pi * i / len(graffiti))) - font_size / 2

        # Draw the letter with a random color and font size
        draw.text((x, y), character, font=font, fill=color)


# Algorithm logic
graffiti = generate_graffiti(characters, colors)
draw_graffiti(graffiti)

# Add spray paint-like texture to the image
image = image.convert("RGB")  # Convert image to RGB mode
image = image.filter(ImageFilter.GaussianBlur(radius=5))
pixels = image.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        r += random.randint(-50, 50)
        g += random.randint(-50, 50)
        b += random.randint(-50, 50)
        pixels[x, y] = (r, g, b)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
