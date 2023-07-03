from main import *

# Image size
WIDTH = 256
HEIGHT = 256


def generate_image(width, height, color):
    image = Image.new('RGB', (width, height), color)
    return image


def save_image_to_file(image, filename):
    image.save(filename)


# Define limited color palette
COLOR_PALETTE = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]


def get_closest_color(color):
    color_distances = []
    for c in COLOR_PALETTE:
        dist = ((c[0] - color[0]) ** 2 + (c[1] - color[1]) ** 2 + (c[2] - color[2]) ** 2) ** 0.5
        color_distances.append(dist)
    closest_color_index = color_distances.index(min(color_distances))
    return COLOR_PALETTE[closest_color_index]


# Generate pixel art
def generate_pixel_art():
    # Generate image
    image = generate_image(WIDTH, HEIGHT, (0, 0, 0))
    draw = ImageDraw.Draw(image)
    # Draw pixels
    for x in range(0, WIDTH, 8):
        for y in range(0, HEIGHT, 8):
            # Get color of a random pixel in the 8x8 block
            block_color = image.getpixel((x + 3, y + 3))
            # Get closest color from the palette
            closest_palette_color = get_closest_color(block_color)
            # Draw pixel
            draw.rectangle((x, y, x + 8, y + 8), fill=closest_palette_color)

    # Save Image to a local file
    save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))


generate_pixel_art()
