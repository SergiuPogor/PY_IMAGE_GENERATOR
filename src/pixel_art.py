from main import *

# Example usage
width = WIDTH
height = HEIGHT

image = generate_image(width, height)
draw = ImageDraw.Draw(image)

# Pixel size
pixel_size = 30

# Define the color palette
palette = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Generate pixel art
for y in range(height):
    for x in range(width):
        # Choose a random color from the palette
        color = random.choice(palette)

        # Calculate the pixel coordinates
        pixel_x = x * pixel_size
        pixel_y = y * pixel_size

        # Draw the pixel
        draw.rectangle([(pixel_x, pixel_y), (pixel_x + pixel_size - 1, pixel_y + pixel_size - 1)], fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
