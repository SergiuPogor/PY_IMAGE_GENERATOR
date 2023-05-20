import noise

from main import *

# Example usage
image_width = WIDTH
image_height = HEIGHT

image = generate_image(image_width, image_height)
draw = ImageDraw.Draw(image)

# Noise parameters
scale = 0.1  # Controls the level of detail in the noise pattern
octaves = 6  # Number of levels of detail in the noise pattern
persistence = 0.5  # Controls the roughness of the noise pattern

# Generate noise-based effects
for y in range(image_height):
    for x in range(image_width):
        # Generate noise value
        noise_value = noise.pnoise2(x * scale, y * scale, octaves=octaves, persistence=persistence)

        # Map noise value to color intensity (0-255)
        color_value = int((noise_value + 1) * 0.5 * 255)

        # Draw pixel with noise-based color
        draw.point((x, y), fill=(color_value, color_value, color_value))

final_filename = '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
make_dir_if_not_exist(final_filename)

# Save the image
image.save(final_filename, "PNG")

print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + '{}'.format(final_filename))
