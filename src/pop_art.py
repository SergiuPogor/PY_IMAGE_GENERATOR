from main import *

# Image size
WIDTH = 800
HEIGHT = 800

# Define colors in RGB format
COLORS = [(255, 51, 102), (51, 255, 0), (255, 255, 51), (51, 153, 255)]

# Define the size of Ben-Day dots
DOT_SIZE = 10

# Define the distance between Ben-Day dots
DOT_DISTANCE = 25


def generate_image(width, height, background_color):
    # Generate new image
    image = Image.new("RGBA", (width, height), background_color)
    return image


def draw_ben_day_dots(draw, x, y, color):
    # Draw Ben-Day dots
    for i in range(0, 4):
        for j in range(0, 4):
            draw.ellipse((x + i * DOT_DISTANCE - DOT_SIZE, y + j * DOT_DISTANCE - DOT_SIZE, x + i * DOT_DISTANCE + DOT_SIZE, y + j * DOT_DISTANCE + DOT_SIZE), fill=color)


def pop_art(image):
    # Loop through each pixel in the image
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Get the color of the pixel
            r, g, b, a = image.getpixel((x, y))

            # Check if the pixel is transparent
            if a == 0:
                continue

            # Choose random color from COLORS list
            color = random.choice(COLORS)

            # Draw Ben-Day dots with the chosen color
            draw_ben_day_dots(draw, x, y, color)

            # Draw an exaggerated shape around the pixel with the same color
            draw.line((x - 5, y - 5, x + 5, y - 5, x + 5, y + 5, x - 5, y + 5, x - 5, y - 5), fill=color, width=3)


if __name__ == "__main__":
    # Image size
    width = WIDTH
    height = HEIGHT

    # Generate new image
    image = generate_image(width=width, height=height, background_color=(255, 255, 255, 255))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Apply pop art effect
    pop_art(image)

    # Save Image to a local file
    save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

